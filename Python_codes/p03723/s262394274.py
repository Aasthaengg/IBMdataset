a,b,c = map(int,input().split(" "))
n = 0
if a % 2 == 1:
    print(0)
    exit()
if b % 2 == 1:
    print(0)
    exit()
if c % 2 == 1:
    print(0)
    exit()
if a == b == c:
  print(-1)
  exit()
for i in range(10**9):
  aa = a//2
  bb = b//2
  cc = c//2
  a = bb + cc
  b = aa + cc
  c = aa + bb
  n += 1
  if a % 2 == 1:
    break
  if b % 2 == 1:
    break
  if c % 2 == 1:
    break
print(n)
