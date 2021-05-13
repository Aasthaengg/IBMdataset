ab = input().split()
a,b = int(ab[0]),int(ab[1])
d = []
z = b - a 
if ((z-1)*z)/2 >a and ((z+1)*(z+2))/2 > b:
    x,y = ((z-1)*z)/2, ((z+1)*(z+2))
print(int(x - a))