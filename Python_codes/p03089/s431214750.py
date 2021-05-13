n=int(input())
b=list(map(int,input().split()))
ans=[]
flg=True
while len(b)>0 and flg:
  n1=len(b)
  i=n1
  flg=False
  while i > 0:
    if b[i-1]==i:
      ans.append(b[i-1])
      b1=b[:i-1]
      b1[len(b1):len(b1)]=b[i:]
      b=b1
      i=-1
      flg=True
    else:
      i-=1

if flg==False:
  print(-1)
  #print(ans)
  exit()
for _ in range(n):
  print(ans.pop())