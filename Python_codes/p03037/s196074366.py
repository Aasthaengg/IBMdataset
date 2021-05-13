N,M = map(int,input().split())
L = []
R = []
for _ in range(M):
    a,b = map(int,input().split())
    L.append(a)
    R.append(b)

if min(R) - max(L) >= 0:
    print(min(R) - max(L) + 1)
else:
    print(0)