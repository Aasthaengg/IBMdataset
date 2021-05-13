N, T = map(int,input().split())
t = list(map(int,input().split()))
res = 0
now = 0
for i in range(N-1):
    if t[i+1]-t[i] <= T:
        res += t[i+1]-t[i]
    else:
        res += T
print(res+T)

