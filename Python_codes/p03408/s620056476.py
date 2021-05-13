def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from collections import Counter

N = INT()
s = [input() for _ in range(N)]
M = INT()
t = [input() for _ in range(M)]

s = Counter(s)
t = Counter(t)
ans = 0

for k, v in s.items():
    ans = max(ans, v - t[k])
    
print(ans)