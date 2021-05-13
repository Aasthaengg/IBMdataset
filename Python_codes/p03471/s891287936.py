n,Y=map(int, input().split())
a=-1,-1,-1
for x in range(n+1):
    for y in range(n-x+1):
      z=n-x-y
      if 10000*x+5000*y+1000*z==Y:
        a=x,y,z
        break
print(*a)