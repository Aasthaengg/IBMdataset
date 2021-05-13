N,T = map(int,input().split())
ts = list(map(int,input().split()))
c = 0
for i in range(1,N):
    if ts[i] - ts[i-1] < T:
        c += ts[i] - ts[i-1]
    else:
        c += T
print(c+T)
