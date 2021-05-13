from collections import Counter

n = int(input())
s = input()
mod = 10**9+7

c = Counter(s)

point = 1

for i,j in c.items():
    point *= j+1
    point %= mod

point -= 1
print(point)