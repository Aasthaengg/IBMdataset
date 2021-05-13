N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
for n in range(N-1):
    if t[n+1]-t[n] >= T:
        ans += T
    else:
        ans += t[n+1]-t[n]
        
print(ans+T)