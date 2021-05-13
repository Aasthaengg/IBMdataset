n=int(input())
d=list(map(int,input().split()))
m=int(input())
t=list(map(int,input().split()))
import collections
d=collections.Counter(d)
t=collections.Counter(t)
for i in t.items():
  if i[0] not in d:
    print("NO")
    break
  elif i[0] in d and i[1]>d[i[0]]:
    print("NO")
    break
else:
  print("YES")
