N, T = map(int, input().split())
A = [int(i) for i in input().split()]

ml = [(A[-1], 1)]
for a in A[-2:0:-1]:
    n = ml[-1]
    if n[0] == a:
        ml.append((a, n[1] + 1))
    elif n[0] < a:
        ml.append((a, 1))
    else:
        ml.append(n)
ml.reverse()

c = [(ml[i][0] - A[i], ml[i][0], ml[i][1]) for i in range(N - 1)]
c.sort(reverse=True)
max_num = c[0][0]
d = {}
cnt = 0

for m in c:
    if m[0] != max_num:
        break
    cnt += 1
    if m[1] not in d:
        d[m[1]] = m[2]
    else:
        d[m[1]] = max(d[m[1]], m[2])

print(min(cnt, sum(d.values())))