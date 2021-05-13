n,k=map(int,input().split())
a=sorted([list(map(int,input().split())) for i in range(n)])
s=0
for x in a:
  if k<=s+x[1]:
    print(x[0])
    break
  s+=x[1]