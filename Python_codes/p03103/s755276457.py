n, m=map(int, input().split())
l=[]
for i in range(n):
  l.append(list(map(int, input().split())))
l = sorted(l, reverse=False)  
#print(l)
drinks=0
ttl=0
add=0
for i in range(n):
  add=min(m-drinks, l[i][1])
  ttl=ttl+add*l[i][0]
  drinks+=add
  if drinks==m:
    print(ttl)
    exit()
