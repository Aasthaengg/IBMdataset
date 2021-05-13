w, a, b = map(int, input().split())
ans = 0
if a < b:
  if a+w > b:
    ans = 0
  else:
    ans = b - (a+w)
elif a == b:
  ans = 0
 
else:
  if b+w > a:
    ans = 0
  else:
    ans = a - (b+w)
 
print(ans)