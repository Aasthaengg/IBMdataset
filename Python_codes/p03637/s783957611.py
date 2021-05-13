N = input()
L = list(map(int,input().split()))
n=0
m=0
p=0
for a in range(int(N)):
  if L[a]%2 != 0:
    n+=1
  elif L[a]%2 == 0 and L[a]%4 != 0:
    m+=1
  else:
    p+=1
if int(N)%2==1 and (n>p+1 or p==0 and n==1):
  print("No")
elif int(N)%2==0 and n>p:
  print("No")
else:
  print("Yes")
