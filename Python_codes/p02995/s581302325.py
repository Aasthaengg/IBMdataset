A,B,C,D=map(int,input().split())

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

cnt_C=B//C-(A-1)//C
cnt_D=B//D-(A-1)//D

lcm_CD=lcm(C,D)
cnt_CD=B//lcm_CD-(A-1)//lcm_CD

ans=(B-A+1)-cnt_C-cnt_D+cnt_CD
print(ans)