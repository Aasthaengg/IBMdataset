a,b,c = map(int,input().split())
r = 0
if a == b == c:
  if a%2 == 1:
    print(r)
    exit()
  else:
    print(-1)
    exit()

while True:
  if a%2 == 1 or b%2 == 1 or c%2 == 1:
    break
  r += 1
  aa = (b+c)//2
  bb = (a+c)//2
  cc = (a+b)//2
  a,b,c = aa,bb,cc

print(r)