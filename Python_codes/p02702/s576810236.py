from collections import defaultdict

S = input()
S = S[::-1]
N = len(S)
memo = defaultdict(int)
memo[0] = 1
ans = 0
rest = 0
for i in range(N):
    rest += int(S[i])*pow(10,i,2019)
    rest %= 2019
    ans += memo[rest]
    memo[rest] += 1
print(ans)

