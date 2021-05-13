# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# まずは桁数を増やす→数字の大きい順に並べる
N, M = lr()
A = lr()
matches = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
A = [(matches[a], a) for a in A]
A.sort(key = lambda x: x[1], reverse=True)
A.sort(key = lambda x: x[0])
top_match = A[0][0]
dp = [None] * (N+1)
dp[0] = []
used = set()
for match, num in A:
    if match in used:
        continue
    used.add(match)
    for x in range(N+1):
        if x - match < 0:
            continue
        if dp[x] == None and dp[x-match] != None:
            dp[x] = dp[x-match] + [num]
        elif dp[x] != None and dp[x-match] != None:
            if len(dp[x-match]) >= len(dp[x]):
                dp[x] = dp[x-match] + [num]
            elif len(dp[x-match]) >= 1 and len(dp[x-match]) == len(dp[x]) - 1:
                y = list(map(str, dp[x][::-1])); y.sort(reverse=True)
                z = [str(num)] + list(map(str, dp[x-match][::-1])); z.sort(reverse=True)
                y = int(''.join(y))
                z = int(''.join(z))
                if z > y:
                    dp[x] = dp[x-match] + [num]

X = dp[N]
X.sort(reverse=True)
answer = ''.join(list(map(str, X)))
print(answer)
# 37
