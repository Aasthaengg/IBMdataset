from collections import defaultdict

N = int(input())
Ds = defaultdict(int)
for k in list(map(int, input().split())):
    Ds[k] += 1
M = int(input())
Ts = defaultdict(int)
for k in list(map(int, input().split())):
    Ts[k] += 1
ans = 'YES'
for k in Ts:
    if Ts[k] > Ds[k]:
        ans = 'NO'
        break
print(ans)
