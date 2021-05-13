import sys
S=list(input())
for i in range(4):
  t=S.count(S[i])
  if t!=2:
    print("No")
    sys.exit()
print("Yes")