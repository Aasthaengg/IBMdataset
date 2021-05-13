a=[]
n=int(input())
b=list(map(int,input().split()))

l=[]
flg=0

for i in range(n-1,-1,-1):
  #print(i,"kocchi",b)
  flg=0
  for j in range(i,-1,-1):
    #print(j,"acchi")
    if j+1==b[j]:
      flg=1
      l.append(b.pop(j))
      break
  if flg==0:
    break

if flg==0:
  print(-1)
else:
  for i in range(n-1,-1,-1):
    print(l[i])
