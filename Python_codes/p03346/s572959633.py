n=int(input())
p=[int(input()) for _ in range(n)]
d={}
for pi in p:
  if pi-1 in d:
    d[pi]=d[pi-1]+1
  else:
    d[pi]=1
print(n-max(d.values()))