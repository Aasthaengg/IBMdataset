def cin():  return list(map(int,input().split()))

N, K = cin()
S = input()

cnt = 0
for i in range(1, N):
    if S[i - 1] == S[i]:  cnt += 1
ans = min(N - 1, cnt + 2 * K)
print(ans)