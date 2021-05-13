a, b = map(int, input().split())

ans = a+b
if ans >= 10:
  ans = 'error'

print(ans)