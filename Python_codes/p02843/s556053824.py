import itertools
x = int(input())
k = x%100
n = x//100
ans = 0
if n*5>=k and n!=0:
    ans = 1
print(ans)