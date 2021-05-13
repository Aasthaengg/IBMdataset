N,H=list(map(int,input().split()))
sword=[list(map(int,input().split())) for i in range(N)]
through=[i[1] for i in sword]
through.sort(reverse=True)
max_atk=max([i[0] for i in sword])
ans=0
for i in through:
   ans+=1
   if i > max_atk:
      H-=i
   else:
      H-=max_atk
   if H <= 0:
      break
import math
if 0 < H:
   ans+=math.ceil(H/max_atk)
print(ans)