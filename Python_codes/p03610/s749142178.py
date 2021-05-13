s =input()

N=len(s)
slist=[]

for i in range(N):
  if i%2==0:
    slist.append(s[i])

M=len(slist)
ans=''
for i in range(M):
  ans=ans+slist[i]
print(ans)