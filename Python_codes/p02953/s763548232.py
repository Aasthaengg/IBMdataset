n= int(input())
if n==1:
  print('Yes')
  exit()
h=list(map(int,input().split()))
ans='Yes'
for i in range(n-1):
  if h[i+1]>h[i]:
    h[i+1]-=1
  elif h[i+1]<h[i]:
    print('No')
    exit()
print(ans)