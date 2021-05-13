from collections import Counter
n = int(input())
D = list(map(int,input().split()))
m = int(input())
T = list(map(int,input().split()))
sd = set(D)
st = set(T)
cntd = Counter(D)
cntt = Counter(T)
ok = True
for t in T:
    if t not in sd:
        ok = False
    elif cntt[t] > cntd[t]:
        ok = False
if ok:
    print('YES')
else:
    print('NO')