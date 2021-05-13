H,W=map(int,input().split())
L=['#'*(W+2)]

for _ in range(H):
  L.append('#'+input()+'#')
else:
  L.append('#'*(W+2))

for l in L:
  print(l)