n,m,k=map(int,input().split())

def black(x,y):
  return x*y+(n-x)*(m-y)

for i in range(n+1):
  for j in range(m+1):
    if black(i,j)==k:
      print("Yes")
      exit()
      
print("No")