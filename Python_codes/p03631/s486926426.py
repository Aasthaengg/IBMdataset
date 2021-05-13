N=input()
flag=0
for i in range(int(len(N)/2)):
  if N[i]!=N[len(N)-1-i]:
    flag=1
    break
  
if flag==0:
  print("Yes")
else:
  print("No")