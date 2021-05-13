#A - Divide a Cuboid 
ABC = list(map(int,input().split()))
ABC = sorted(ABC,reverse = True)
A,B,C = ABC[0],ABC[1],ABC[2]
a,b,c = A%2,B%2,C%2

if a == 0 or b == 0 or c == 0:
    diff = 0
else:
    b = (A//2)*B*C
    r = ((A+2-1)//2)*B*C
    diff = r-b
print(diff)