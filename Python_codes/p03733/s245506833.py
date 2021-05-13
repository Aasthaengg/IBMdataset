N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = T*N
for i in range(N-1):
    ans -= max(T-(t[i+1]-t[i]), 0)
print(ans)