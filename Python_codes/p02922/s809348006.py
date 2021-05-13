a,b = map(int,input().split())
if b == 1:
  print(0)
  exit()
for n in range(1,100):
  if a + (a-1)*(n-1)  >= b:
    print(n)
    exit()