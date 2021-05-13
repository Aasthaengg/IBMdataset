n=int(input())
c=list(input())

cntr=c.count('R')

cnt=0
for i in range(0,cntr):
  if c[i]=='W':
    cnt+=1

print(cnt)