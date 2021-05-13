import bisect

X, N = map(int,input().split())
if N == 0:
    Ps = []
else:
    Ps = list(map(int,input().split()))
Ps.sort()
for i in range(300):
    if i % 2 == 0:
        x = i//2
    else:
        x = -((i+1)//2)
    if (X + x) in Ps:
        continue
    else:
        print(X + x)
        break
