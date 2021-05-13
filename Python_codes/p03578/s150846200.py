from collections import Counter

n = int(input())
dl = list(map(int, input().split()))
m = int(input())
tl = list(map(int, input().split()))

ts = list(set(tl))
tc = Counter(tl)
dc = Counter(dl)

for t in ts:
    if tc[t] <= dc[t]:
        continue
    else:
        print('NO')
        break
else:
    print('YES')