N=int(input())
A=[]
for i in range(N):
  A.append(int(input()))
A.sort(reverse=True)
ans=sum(A)
if ans%10!=0:
  print(ans)
  exit()
else:
  for i in range(N):
    tmp=ans-A[-(i+1)]
    if tmp%10!=0:
      print(tmp)
      exit()
print(0)