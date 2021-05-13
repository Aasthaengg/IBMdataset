h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

ansli=[]
ans=[]
for i in range(n):
  for j in range(a[i]):
    ansli.append(i+1)

for i in range(h):
  temp=ansli[0+i*w:(i+1)*w]
  if not i%2:
    ans.append(temp)
  else:
    ans.append(temp[::-1])

for i in ans:
  print(*i)