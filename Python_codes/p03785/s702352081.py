N,C,K=list(map(int,input().split()))
import sys
l=[r.rstrip() for r in sys.stdin.readlines()]
l=list(map(int,l))
l.sort()
ans=0
now=0
for i in range(N):
   X=l[now]
   for j in range(C):
      if X <= l[now] <= X+K:
         now+=1
         if now==N:
            break
      else:
         break
   ans+=1
   if now==N:
      break
print(ans)