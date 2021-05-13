N=int(input())
B=[int(i) for i in input().split()]
TF=[True for _ in range(N)]
I=list(reversed(range(N)))
ans=[]
d=0
while N!=d:
  # print(TF)
  flag=True # -1 flag
  k=d
  for i in I:
    # print(d,k,i)
    if TF[i]:
      if i+1-k==B[i]:
        TF[i]=False
        flag=False
        ans.append(i)
        d+=1
        break
    else:
      k-=1
  if flag:
    ans=-1
    break
if ans==-1:
  print(ans)
else:
  for i in reversed(ans): print(B[i])