n,a,b,c,d=map(int,input().split())
s=input()
flag=0
for i in range(n):
  if a-1<=i<=c-1 or b-1<=i<=d-1:
    if flag==1 and s[i]=="#":
      print("No")
      exit()
    elif flag==0 and s[i]=="#":
      flag=1
    elif s[i]==".":
      flag=0

m=0
con=0
if d<c:
  for i in range(b-2,d+1):
    if s[i]==".":
      con+=1
      m=max(m,con)
    else:
      con=0
  if m>=3:
    print("Yes")
    exit()
  else:
    print("No")
    exit()
print("Yes")