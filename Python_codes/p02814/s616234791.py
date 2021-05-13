from fractions import gcd

def calc_half(n):
    return n//2

def lcm(L):
    ret=1
    for i in range(len(L)):
        ret=(ret*L[i])//gcd(ret,L[i])
    return ret

def f(n):
    ret=0
    while n%2==0:
        ret+=1
        n=n//2
    return ret

def g(L):
    l=[]
    for i in L:
        l.append(f(i))
    if len(set(l))==1:
        return False
    else:
        return True

n,m=map(int,input().split())
A=list(map(int,input().split()))
Auniq=list(set(A))
Ahalf=list(map(calc_half,Auniq))
lcm_ori=lcm(Auniq)
lcm_half=lcm(Ahalf)

if m<lcm_half or g(Auniq):
    print("0")
else:
    print(1+(m-lcm_half)//lcm_ori)