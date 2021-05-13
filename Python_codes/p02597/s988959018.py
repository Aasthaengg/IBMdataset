N=int(input())
C=input()
s=0
e=N-1
ans=0
while(s<e):
  while(C[s]=="R" and s<e):
    s+=1
  while(C[e]=="W" and s<e):
    e-=1
  if s<e:
    s+=1
    e-=1
    ans+=1
print(ans)