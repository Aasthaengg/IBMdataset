x,y = map(int,input().split())
r = 1
for i in range(1,10**3):
  if x * r > y:
    print(i-1)
    exit()
  r *= 2