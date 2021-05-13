S=input()
N=len(S)
post=S[0]
ans=1
now=""
for i in range(1,N):
  now+=S[i]
  if post!=now:
    post=now
    now=""
    ans+=1
print(ans)


