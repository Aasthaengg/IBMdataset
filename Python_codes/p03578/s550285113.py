from collections import Counter
n = int(input())
d = dict(Counter(list(map(int,input().split()))))
m = int(input())
t = list(map(int,input().split()))
check = True
for i in t:
  if i in d.keys():
    if d[i] > 0:
      d[i] -= 1
    else:
      check = False
      break
  else:
    check = False
    break
print("YES" if check else "NO")