a,b,k=map(int,input().split())
ans=[]
i=0
while i<k and a+i<=b-i:
  ans.append(a+i)
  ans.append(b-i)
  i=i+1
ans=list(set(ans))
ans.sort()
for i in range(0,len(ans)):
  print(ans[i])