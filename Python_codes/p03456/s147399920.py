import sys
a,b=map(str,input().split())
ans=[]
for i in range(len(a)):
  ans.append(a[i])
for i in range(len(b)):
  ans.append(b[i])
n=int(''.join(ans))
i=0
while i*i<=n:
  if i*i==n:
    print('Yes')
    sys.exit()
  i+=1
print('No')