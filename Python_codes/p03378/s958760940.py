N,gate,start=list(map(int,input().split()))
W=list(map(int,input().split()))
le=0
ri=0
for i in range(start,N+1):
  if i in W:
    ri+=1
for k in range(start+1):
  if k in W:
    le+=1
print(min(ri,le))