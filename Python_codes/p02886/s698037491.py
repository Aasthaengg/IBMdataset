from itertools import combinations

n = int(input())
d = list(map(int,input().split()))

nc2 = list(combinations(d,2))
comb_sum = 0
for x,y in nc2:
  comb_sum += x * y
print(comb_sum)