nk = input().split()
n = int(nk[0])
k = int(nk[1])

dtlist = []
for i in range(n):
    td = input().split()
    t = int(td[0])
    d = int(td[1])
    dtlist.append((d, t))
dtlist.sort(reverse=True)


t_to_maxidx = {}
for idx, dt in enumerate(dtlist):
    d, t = dt
    if t not in t_to_maxidx:
        t_to_maxidx[t] = idx


selected = []
count = 0
tcount = {}

candidate = [(dtlist[idx][0], idx) for t, idx in t_to_maxidx.items()]
candidate.sort(reverse=True)
for d, idx in candidate:
    if count >= k:
        break
    d, t = dtlist[idx]
    selected.append(dtlist[idx])
    count += 1
    tcount[t] = 1 if t not in tcount else tcount[t] + 1
    dtlist[idx] = None

new_dtlist = []
for dt in dtlist:
    if dt is not None:
        new_dtlist.append(dt)
dtlist = new_dtlist


if k - count > 0:
    for i in range(k - count):
        dt = dtlist.pop(0)
        selected.append(dt)
        d, t = dt
        tcount[t] = 1 if t not in tcount else tcount[t] + 1

selected.sort()

score = 0
for d, t in selected:
    score += d

len_tcount = len(tcount)
score += len_tcount * len_tcount

for i in range(0, 2**32):
    next_score = score
    try:
        d_new, t_new = dtlist.pop(0)
        d_old, t_old = selected.pop(0)
    except IndexError:
        print(score)
        break
    next_score += d_new
    next_score -= d_old

    tcount[t_old] -= 1
    if tcount[t_old] <= 1:
        next_score -= len_tcount * len_tcount
        len_tcount -= 1
        next_score += len_tcount * len_tcount
        del tcount[t_old]

    if t_new not in tcount:
        next_score -= len_tcount * len_tcount
        len_tcount += 1
        next_score += len_tcount * len_tcount
        tcount[t_new] = 1
    else:
        tcount[t_new] += 1

    if next_score <= score:
        print(score)
        break
    score = next_score
