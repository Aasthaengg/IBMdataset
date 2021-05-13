from collections import Counter
n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

d_count = Counter(d)
t_count = Counter(t)
for x,y in t_count.items():
  if x in d_count:
    if y > d_count[x]:
      print("NO")
      break
  else:
    print("NO")
    break
else: print("YES")