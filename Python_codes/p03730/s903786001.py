A, B, C = map(int, input().split())
rm = A%B
flag = False
for i in range(B):
  if (A*(i+1)%B == C):
    flag = True
if (flag):
  print("YES")
else:
  print("NO")