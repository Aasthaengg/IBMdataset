N, A, B = map(int, input().split())
ans = 'Alice'
if (B - A) % 2 == 1:
  ans = 'Borys'
print(ans)