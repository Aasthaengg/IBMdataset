n=int(input())
lipp = []
lipm = []
limm = []
allcnt = 0
for _ in range(n):
    s = input()
    cnt = 0
    mi = 0
    for x in s:
        if x == ')':
            cnt -= 1
            mi = min(mi,cnt)
        else:
            cnt += 1
    if mi == 0:
        lipp.append(cnt)
    elif cnt >= 0:
        lipm.append([mi,cnt])
    else:
        limm.append([cnt - mi, mi,cnt])
    allcnt += cnt
if allcnt != 0:
    print('No')
    exit()

now = sum(lipp)
lipm.sort(reverse = True)
limm.sort()

for mi, cnt in lipm:
    if mi + now < 0:
        print('No')
        exit()
    now += cnt

cnt2 = 0
for sa, mi, cnt in limm:
    if sa > cnt2:
        print('No')
        exit()
    cnt2 += -cnt
print("Yes")