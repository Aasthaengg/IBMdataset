import sys
a,b,c = map(int,input().split())
ans = 0
pa = []
pb = []
while True:
  if a%2 == 1 or b%2 == 1 or c%2 == 1:
    break
  ans += 1
  lasta = a
  lastb = b
  lastc = c
  a = lastb/2 + lastc/2
  b = lasta/2 + lastc/2
  c = lasta/2 + lastb/2
  for i in range(len(pa)):
    if pa[i] == a:
      if pb[i] == b:
        print(-1)
        sys.exit()
  pa.append(a)
  pb.append(b)
print(ans)