n=int(input())
ans=[]
s=n+1-n%2
for i in range(1,n+1-n%2):
  for j in range(i+1,n+1-n%2):
    if i+j==s:
      continue
    ans.append(str(i)+" "+str(j))
if n%2:
  for i in range(1,n):
    ans.append(str(i)+" "+str(n))
print(len(ans))
print("\n".join(ans))