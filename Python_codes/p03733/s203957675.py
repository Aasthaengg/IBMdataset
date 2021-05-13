N, T = map(int, input().split())
swc = list(map(int, input().split()))
ans = 0
for i in range(N-1):
    if swc[i+1] - swc[i] < T:
        ans += (swc[i+1] - swc[i])
    else:
        ans += T
print(ans+T)