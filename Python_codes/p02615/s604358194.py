input()
A=list(map(int,input().split()))
A.sort(reverse=True)
B=[]
ans=0
for i in A:
  if len(B)>=1:
    ans+=B[len(B)//2]
  B.append(i)
print(ans)