from decimal import *
A,B,C,D=list(map(int,input().split()))

def gcd(a,b):
    x=max(a,b)
    y=min(a,b)
    
    while True:
#         print(x,y)
        y_ = x % y
        if y_ == 0:
            return y
        x = y
        y = y_

def lcm(a,b):
    ans=Decimal(a*b)/Decimal(gcd(a,b))
    return ans.as_integer_ratio()[0]

CD=lcm(C,D)
len_all = B-A+1
len_c = B//C-(A-1)//C
len_d = B//D-(A-1)//D
len_c_and_d = B//CD-(A-1)//CD

ans=len_all-len_c-len_d+len_c_and_d 
print(int(ans))