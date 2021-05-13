N, K = list(map(int,input().split()))
S = input()
ans = 0
for i in range(1, N):
    if S[i] == "R" and S[i - 1] == "R":  ans += 1
for i in range(1, N):
    if S[i] == "L" and S[i - 1] == "L":  ans += 1
ans = min(ans + 2 * K, N - 1)
print(ans)