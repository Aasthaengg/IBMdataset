X=input()

ans=0
a=0
for i in range(len(X)):
  if(X[i]=="T"):
    a+=1
  else:
    a-=1
  ans=max(ans,a)
print(ans*2)