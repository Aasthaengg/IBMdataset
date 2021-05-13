def cnt_div2(n):
    cnt=0
    while n%2==0:
        n//=2
        cnt+=1
    return cnt
def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while b:
        a,b = b,a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

N,M = map(int,input().split())
A = list(map(lambda x:int(x)//2,input().split()))

if(all(cnt_div2(A[0]) == cnt_div2(a) for a in A)):
    if N==1:
        lcm_A = A[0]
    else:
        lcm_A = lcm(A[0],A[1])
        for a in A[2:]:
            lcm_A = lcm(lcm_A,a)
    print(int((M/lcm_A+1)//2))
else:
    print(0)

