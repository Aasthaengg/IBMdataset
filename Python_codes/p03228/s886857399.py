def ex(a,b,n):
  for _ in range(n):
    a, b = b + a//2, a//2
  if n%2:
    a,b = b,a
  return str(a),str(b)
a, b, k = map(int, input().split())
print(' '.join(ex(a,b,k)))
