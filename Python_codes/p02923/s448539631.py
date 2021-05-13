N = int(input())
H = list(map(int, input().split()))

H.append(10**10) 
r, ans = 0, 0
for l in range(N):
    while r < N and H[r] >= H[r+1]:
        r += 1
    ans = max(ans, r-l)
    if l == r:
        r += 1
print(ans)