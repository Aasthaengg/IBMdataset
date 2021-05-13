a,b = map(float,input().split())
for i in range(10000):
  c = i*8//100
  d = i*10//100
  if(a == c and b == d):
    print(i)
    exit()
print(-1)