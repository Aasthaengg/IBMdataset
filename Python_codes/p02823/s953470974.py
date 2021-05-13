N, A, B = map(int, input().split())

Abs = B - A
if Abs % 2 == 0:
  ans = Abs // 2
else:
  a, b = A-1, N-B
  if a < b:
    ans, B = a+1, B-(a+1)
    ans += (B-1) // 2
  else:
    ans, A = b+1, A+(b+1)
    ans += (N-A) // 2
    
print(ans)