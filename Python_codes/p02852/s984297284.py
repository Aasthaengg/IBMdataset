N,M=map(int,input().split())
S=list(map(int,list(input())))

ans=[]
ind=N
while ind>0:
  j=0
  for i in range(max(ind-M,0),ind):
    if S[i]==0:
      ans.append(ind-i)
      ind=i
      j=1
      break
  if j==0:
    print(-1)
    exit()
      
print(*reversed(ans))