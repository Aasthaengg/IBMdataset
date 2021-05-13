h = int(input())
w = int(input())
n = int(input())
ans = 0
if h >= w :
  if n%h != 0:
    ans = (n//h) +1
  else:
    ans = n//h
elif  w > h:
  if n%w != 0:
    ans  = (n//w) +1
  else:
    ans = n//w
print(ans)