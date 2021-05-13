import sys
n=int(input())
h=list(map(int,input().split()))
if h[0]>0:
  h[0]-=1
for i in range(1,n):
  if h[i-1]==h[i]:
    sonomama=1
  elif h[i]>h[i-1]:
    h[i]-=1
  else:
    print("No")
    sys.exit()
print("Yes")
    
