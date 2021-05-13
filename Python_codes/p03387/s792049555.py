a,b,c = [int(x) for x in input().split()]
res = 3 * max(a,b,c) - (a + b + c)
if res % 2 == 1:
  res += 3
print(res // 2)