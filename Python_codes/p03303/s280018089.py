S=input()
w=int(input())

ans=S[0]

for i in range(1,len(S)):
  if i%w==0:
    ans+=S[i]
print(ans)