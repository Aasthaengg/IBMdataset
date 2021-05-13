from collections import defaultdict
S = input()
S = S[::-1]

rest = 0
ans = 0
memo = defaultdict(int)
memo[0] = 1
for i in range(len(S)):
    rest = (rest + int(S[i])*pow(10,i,2019)) %2019
    ans += memo[rest]
    memo[rest] += 1
print(ans)