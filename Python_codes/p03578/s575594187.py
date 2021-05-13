n=int(input())
a=list(map(int,input().split()))
from collections import Counter
d=Counter(a)
m=int(input())
b=list(map(int,input().split()))
dd=Counter(b)
for i in dd:
  if i not in d:
    print("NO")
    exit()
  if d[i]<dd[i]:
    print("NO")
    exit()
print("YES")