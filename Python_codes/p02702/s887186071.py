"""
dp的な発想で解けるかな？
下の桁から見る。桁を一つずつ
"""
from collections import defaultdict
S = input()
N = len(S)
S = S[::-1]

ans = 0
memo = defaultdict(int)
num = 0
memo[0] = 1
for i in range(N):
    num = (num+(pow(10,i,2019)*int(S[i]))%2019)%2019
    ans += memo[num]
    memo[num] += 1

print(ans)