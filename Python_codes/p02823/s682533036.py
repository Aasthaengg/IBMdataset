n,a,b = map(int,input().split())

if a == b:
  ans = 0
elif abs(a-b)%2 == 0:
  ans = abs(a-b)//2
elif abs(a-b)%2 == 1:
  if a > b:
    if (a-1) > (n-b):
      ans = (n-a) + (a-b-1)//2 + 1
    else:
      ans = (b-1) + (a-b-1)//2 + 1
  if b > a:
    if (b-1) > (n-a):
      ans = (n-b) + (b-a-1)//2 + 1
    else:
      ans = (a-1) + (b-a-1)//2 + 1
      
print(ans)