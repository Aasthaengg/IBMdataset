N,M=map(int, input().split())

D={} 
for i in range(N):
  D[i+1]=0
for i in range(M):
  a,b=map(int, input().split())
  D[a]+=1
  D[b]+=1

odds=0
evens=0
for v in D.values():
    if v%2==0:
        evens+=1
    else:
        odds+=1
if odds>0:
    print("NO")
else:
    print("YES")