a,b=map(int,input().split())
c=int(str(a)+str(b))
for i in range(int(c**(1/2))+1) :
  if i**2==c :
    print("Yes")
    exit()
print("No")