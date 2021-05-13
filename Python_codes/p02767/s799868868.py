n = int(input())
aaa = list(map(int, input().split(' ')))
center = sum(aaa) // n
ans = 99999999999999999
for i in [-1, 0, 1]:
  ans = min(ans, sum([(a - center + i) ** 2 for a in aaa]))
  
print(ans)