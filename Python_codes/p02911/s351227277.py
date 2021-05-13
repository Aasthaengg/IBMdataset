n,k,q=map(int,input().split())
a=[int(input()) for i in range(q)]

m=[0]*n

for i in range(q):
  m[a[i]-1]+=1

for j in range(n):
  m[j]=k+m[j]-q

ans=['No']*n

for h in range(n):
  if m[h]>0:
    ans[h]='Yes'

print('\n'.join(ans))