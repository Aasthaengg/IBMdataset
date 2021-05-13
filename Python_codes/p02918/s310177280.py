N,K=map(int, input().split())
S=input()
comp=[]
tmp=""

for i in range(N):
  if tmp=="":
    tmp=S[i]
    cnt=1
  else:
    if S[i]==tmp:
      cnt +=1
      
  if S[i]!=tmp:
    comp.append([tmp,cnt])
    tmp=S[i]
    cnt=1
  if i==N-1:
    comp.append([tmp,cnt])
  
ans=0  
for run in comp:
  ans += run[1]-1
ans += K*2
ans = min(ans,N-1)
print(ans)