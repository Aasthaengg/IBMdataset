n,m=map(int,input().split())
e=[[] for _ in range(n)]
b=[]

for i in range(m):
  x,y=map(int,input().split())
  e[x-1].append(y-1)
  e[y-1].append(x-1)
  b.append([x-1,y-1])

def ne(now,s,visit):
  visit.append(now)
  for i in e[now]:
    if i not in visit:
      ne(i, s, visit[:])
    elif len(visit)>2 and s==i:
      v1=visit[1]
      v2=visit[-1]
      if [s,v1] in b: b.remove([s,v1])
      elif [v1,s] in b: b.remove([v1,s])
      if [s,v2] in b:b.remove([s,v2])
      elif [v2,s] in b:b.remove([v2,s])
      break

for i in range(n):
  ne(i,i,[])
print(len(b))