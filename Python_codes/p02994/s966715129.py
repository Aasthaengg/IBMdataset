n, l = map(int, input().split())
apple = list(range(l, l + n))
ans = 0
if 0 in apple:
  ans = sum(apple)
elif abs(apple[0]) < abs(apple[-1]):
  ans = sum(apple[1:])
else:
  ans = sum(apple[:-1])
print(ans)