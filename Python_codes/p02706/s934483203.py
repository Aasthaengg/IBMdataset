N,M = map(int,input().split())
A = list(map(int,input().split()))
for a in A:
    N -= a
if N < 0:
    print(-1)
else:
    print(N)
