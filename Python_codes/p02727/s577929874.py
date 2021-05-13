X,Y,A,B,C=list(map(int,input().split()))
A_l=list(map(int,input().split()))
B_l=list(map(int,input().split()))
C_l=list(map(int,input().split()))
A_l.sort(reverse=True)
B_l.sort(reverse=True)
C_l.sort()
A_after_l=A_l[:X]
B_after_l=B_l[:Y]
ans=[A_after_l,B_after_l]
ans=sum(ans,[])
ans.sort()
import heapq
heapq.heapify(ans)
for i in C_l:
   N=heapq.heappop(ans)
   if N < i:
      heapq.heappush(ans,i)
   else:
      heapq.heappush(ans,N)
print(sum(ans))