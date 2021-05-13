x,y,z=map(int,input().split())
c=0
for i in range(100000):
    c=z-i*x
    if c<0:
        break
print((i-1)*y)
    
