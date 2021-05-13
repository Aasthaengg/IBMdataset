# D - Match Matching

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse = True)

n_match = [-1,2,5,5,4,5,6,3,7,6]

dp = [-1] * (N+1) # dp[i]はちょうどi本のマッチ棒で作れる最も桁数の多い整数の桁数

dp[0] = 0
for idx in range(1,N+1):
    tmp = []
    for x in A:
        if idx - n_match[x] >= 0:
            tmp.append(dp[idx - n_match[x]] + 1)
    if tmp:
        dp[idx] = max(tmp)

ans = ""
rest_match = N
while len(ans) <= N//2 and rest_match > 0:
    for x in A:
        if rest_match - n_match[x] >= 0 and dp[rest_match - n_match[x]] == dp[rest_match] - 1:
            ans += str(x)
            rest_match -= n_match[x]
            break
            
print(ans)