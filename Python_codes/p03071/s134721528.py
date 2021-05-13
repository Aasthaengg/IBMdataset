A, B = map(int,input().split())
ans = 0
for i in range(2):
  ans += max(A,B)
  if max(A,B) == A:
    A -= 1
  else:
    B -= 1
print(ans)
