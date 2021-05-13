from collections import Counter 

N=int(input())
C = Counter(list(map(int,input().split())))
O=int(input())
M = Counter(list(map(int,input().split())))
for key in M.keys():
  if C[key]<M[key]:
    print("NO")
    break
else:
  print("YES")
