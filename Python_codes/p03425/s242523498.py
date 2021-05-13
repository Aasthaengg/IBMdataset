def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

from itertools import combinations

N = INT()
march = {}

for ini in "MARCH":
    march[ini] = 0
    
for _ in range(N):
    s = input()
    
    if s[0] in "MARCH":
        march[s[0]] += 1

ans = 0

for comb in combinations(march.values(), 3):
    tmp = 1
    for c in comb:
        tmp *= c
    
    ans += tmp
    
print(ans)