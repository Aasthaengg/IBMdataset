A, B = map(int, input().split())
 
ans = 0
 
while A<=B :
  if str(A)==str(A)[::-1]:
    ans = ans + 1
  else:
    ans = ans
  A = A + 1
 
print(ans)
