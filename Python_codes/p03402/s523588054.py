k=50
l=[["." if h<k else "#" for w in range(2*k)] for h in range(2*k)]
a,b=map(int,input().split())

#a->white. b->black#
aa=0
for y in range(k+1,k*2,2):
  if aa==a-1:break

  for x in range(0,2*k,2):
    if aa==a-1:break
    l[y][x]="."
    aa+=1

bb=0
for y in range(0,k-1,2):
  if bb==b-1:break
  for x in range(0,2*k,2):
    if bb==b-1:break
    l[y][x]="#"
    bb+=1

print(2*k,2*k)
for i in l:
  print("".join(i))