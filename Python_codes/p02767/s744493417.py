import math
n = int(input())
l = list(map(int, input().split()))

av = sum(l)/n
af = math.floor(av)
ac = math.ceil(av)

sf = 0
sc = 0

for i in l:
    sf += (abs(i-af))**2
    sc += (abs(i-ac))**2

print(min(sf,sc))
