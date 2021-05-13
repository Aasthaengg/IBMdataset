N=int(input())
cnt=1
flag=True
while N>=10:
  if N%10!=9:
    flag=False
  N//=10
  cnt+=1
if flag==True:
  ans=N+9*(cnt-1)
else:
  ans=N+9*(cnt-1)-1
print(ans)
