n=int(input())
a=list(map(int,input().split()))
num=0

for i in range(n):
  if a[i]%2==1:
    num+=1
    
if num%2==0:
  print("YES")
elif num%2==1 and n==num:
  print("YES")
else:
  print("NO")