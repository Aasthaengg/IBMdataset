ans = 1
x,y = [int(x) for x in input().split()]
while True:
  if x*(2**ans) > y:
    break
  ans += 1
print(ans)