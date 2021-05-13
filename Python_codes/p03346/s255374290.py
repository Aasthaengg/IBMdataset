n=int(input())
p=[int(input()) for i in range(n)]
l=[-1 for i in range(n)]
for i in range(n):
  l[p[i]-1]=i
ans=[]
ct=1
for i in range(n-1):
  if l[i]<l[i+1]:
    ct+=1
  else:
    ans.append(ct)
    ct=1
ans.append(ct)
ct=1
print(n-max(ans))