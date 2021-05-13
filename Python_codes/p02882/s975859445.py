import math
a,b,x = list(map(int,input().split()))

check = a*a*b/2

if x >= check: 
    ans = math.degrees(math.atan(2*(b/a-x/(a**3))))
else :
    c_=a*b*b/2
    ans = math.degrees(math.atan((c_/x)))
    
print(ans)