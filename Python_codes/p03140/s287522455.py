N=int(input())
A=input()
B=input()
C=input()
ans=0
for i,k,t in zip(A,B,C):
  if i==k==t:
    ans=ans
  elif i!=k and k!=t and t!=i:
    ans+=2
  else:
    ans+=1  
print(ans)