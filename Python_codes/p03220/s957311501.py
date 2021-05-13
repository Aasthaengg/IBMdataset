N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
ans = (10**9, -1)
for i in range(N):
    tmp = T - 0.006 * H[i]
    if abs(tmp - A) < ans[0]:
        ans = (abs(tmp - A), i + 1)
print(ans[1])
