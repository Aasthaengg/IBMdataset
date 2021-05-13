S=input()
ans=0
for i in range(0,4):
  if S[i]=="+":
    ans+=1
  else:
    ans-=1
print(ans)
