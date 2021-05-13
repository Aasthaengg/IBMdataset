from operator import itemgetter
n=int(input())
p=[int(input()) for i in range(n)]
d=dict()
for i in range(n):
  if p[i]-1 not in d:
    d[p[i]]=1
  else:
    d[p[i]]=d[p[i]-1]+1
d=list(d.items())
d.sort(reverse=True,key=itemgetter(1))
print(n-d[0][1])