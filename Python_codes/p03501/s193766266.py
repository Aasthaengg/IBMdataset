n, a, b = map(int, input().split())

if n * a >= b:
  ans = b
elif n * a < b:
  ans = n *a
  
print(ans)