from collections import Counter
n = int(input())
l = Counter(list(map(int,input().split())))
m = int(input())
t = list(map(int,input().split()))
#print(l)
if n<m:
  print("NO")
  exit()
for j in t:
  if ( j in l ) and l[j]>=1:
    l[j] -= 1
 #   print(l)
    continue
  else:
    print("NO")
    exit()
else:
  print("YES")