import math

def getDivCount( a, b, x ):
    count=0
    if a!=0 :
        count+=b//x-(a-1)//x
    else:
        count+=b//x+1
    return count

a,b,c,d = map(int, input().split())

count = b-a+1
count -= getDivCount(a,b,c)
count -= getDivCount(a,b,d)
count += getDivCount(a,b,c*d//math.gcd(c,d))
print(count)
