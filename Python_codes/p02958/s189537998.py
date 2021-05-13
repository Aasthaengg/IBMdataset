N = int(input())
P = list(map(int,input().split()))
Q = sorted(P)
d = 0

for p,q in zip(P,Q):
  if p!=q:
    d+=1

if d<=2:
  print("YES")
else:
  print("NO")