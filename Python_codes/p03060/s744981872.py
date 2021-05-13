n=int(input())
v=list(map(int,input().split()))
c=list(map(int,input().split()))
val=0
for i in range(n):
  xy=v[i]-c[i]
  if xy>0:
    val=val+xy
print(val)