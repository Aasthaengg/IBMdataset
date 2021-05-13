N,M = list(map(int,input().split()))
A = list(map(int,input().split()))
t = N - sum(A)
if t < 0:
    print(-1)
else:
    print(t)