N=int(input())
if N==0:
  print(0)
  exit()
ans=[]
while N!=0:
  tmp=N%(2)
  if tmp<0:
    tmp+=2
  N=(N-tmp)//(-2)
  ans.append(str(tmp))
  
ans=ans[::-1]
Ans=''.join(ans)
print(Ans)