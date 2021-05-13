N= int(input())
A= list(input())
B= list(input())
C= list(input())
ans=0
import collections
for i in range(N):
   l=[A[i],B[i],C[i]]
   l=collections.Counter(l).most_common()
   ans+=3-l[0][1]
print(ans)