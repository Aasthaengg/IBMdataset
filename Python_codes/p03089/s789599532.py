n=int(input())
b=[int(i) for i in input().split()]
ans=[]
while len(b)>0:
  f=0
  for i in range(len(b),0,-1):
    if b[i-1]==i:
      ans.append(i)
      del b[i-1]
      f=1
      break
  if f==0:
    print(-1)
    exit()
print(*ans[::-1],sep='\n')