n = int(input())
v = list(map(int,input().split()))
d1 = {}
d2 = {}

for i in range(0,n//2):
  a1 = v[2*i]
  a2 = v[2*i+1]
  
  if a1 not in d1:
    d1[a1] = 1
  else:
    d1[a1] += 1
    
  if a2 not in d2:
    d2[a2] = 1
  else:
    d2[a2] += 1


l1 = list(sorted(d1.items(), key=lambda x:x[1]))
l2 = list(sorted(d2.items(), key=lambda x:x[1]))


if len(set(v)) == 1:
  print(n//2)
  exit()
if l1[-1][0] == l2[-1][0] and len(l1) >= 2 and len(l2) >= 2:
  print(min(n - l1[-1][1] - l2[-2][1],n - l1[-2][1] - l2[-1][1]))
elif l1[-1][0] == l2[-1][0] and len(l1) == 1 and len(l2) >= 2:
  print(n - l1[-1][1] - l2[-2][1])
elif l1[-1][0] == l2[-1][0] and len(l1) >= 2 and len(l2) == 1:
  print(n - l1[-2][1] - l2[-1][1])
else:
  print(n - l1[-1][1] - l2[-1][1])