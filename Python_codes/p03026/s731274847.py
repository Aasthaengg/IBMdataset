n=int(input())
e=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(lambda x:int(x)-1,input().split())
  e[a].append(b)
  e[b].append(a)
c=list(map(int,input().split()))
c.sort()
print(sum(c[:-1]))

c.reverse()
ans=[0 for i in range(n)]
ans[0]=c[0]
k=1

s=[0]
while s:
  ns=[]
  for i in s:
    for j in e[i]:
      if ans[j]:
        continue
      ans[j]=c[k]
      k+=1
      ns.append(j)
  s=ns
print(" ".join(map(str,ans)))
