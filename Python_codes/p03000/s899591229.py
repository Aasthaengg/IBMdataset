n,x=map(int,input().split())
l=[int(x) for x in input().rstrip().split()]
now=0
cnt=1
for i in range(n):
  now+=l[i]
  if x<now:
    break
  cnt+=1
print(cnt)