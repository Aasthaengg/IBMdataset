n=int(input())
a=list(map(int,input().split()))
q=int(input())
bc=[list(map(int,input().split())) for i in range(q)]

asum=sum(a) #当初の数列Aの要素の和
d={}

for i in a:
  if i in d:
    d[i]+=1
  else:
    d[i]=1

for b,c in bc:
  if b in d:
    asum+=d[b]*(c-b)
    if c in d:
      d[c]+=d[b]
    else:
      d[c]=d[b]
    d[b]=0
  print(asum)