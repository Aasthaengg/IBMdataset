N=int(input())
import collections
D= collections.Counter(list(map(int,input().split())))
M=int(input())
T= collections.Counter(list(map(int,input().split())))
for i,j in T.items():
   if D[i] >= j:
      pass
   else:
      print("NO")
      exit()
print("YES")