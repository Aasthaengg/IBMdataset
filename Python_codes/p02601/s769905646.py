a,b,c = map(int,input().split())
k = int(input())
while(a >= b):
  if k == 0:
    break
  else:
    b *= 2
    k -= 1
while(b >= c and k >= 1):
  if k == 0:
    break
  else:
    c *= 2
    k -= 1
if a < b < c:
  print("Yes")
else:
  print("No")