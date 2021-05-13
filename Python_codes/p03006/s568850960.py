n=int(input())
if n==1:
  print(1)
  exit()
l=[list(map(int,input().split())) for _ in range(n)]
d=[]
for i in range(n):
  for j in range(n):
    if i!=j:
      d.append((l[i][0]-l[j][0],l[i][1]-l[j][1]))
from collections import Counter as c
print(n-c(d).most_common()[0][1])