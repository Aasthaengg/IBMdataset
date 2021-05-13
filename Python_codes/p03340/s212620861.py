N = int(input())
L = list(map(int,input().split()))

r = -1; s = 0
ans = 0
for i in range(N):
    while r < N - 1 and not (s & L[r+1]):
        s ^= L[r + 1]; r += 1
    ans += r - i + 1
    s ^= L[i]
print(ans)
