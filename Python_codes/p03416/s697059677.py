a,b=map(int,input().split())
l=[]
for i in range(a,b+1):
  l.append(i)

def st(n):
  return str(n)

li=list(map(st,l))

ans=0
for j in li:
  if j[0]==j[-1] and j[1]==j[-2]:
    ans+=1
  else:
    pass

print(ans)