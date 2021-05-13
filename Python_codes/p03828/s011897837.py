
mod=10**9+7

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

# ===========================素数判定 1:2以上の素数　,0：倍数    
def isPrime(x):
    if x < 2:
        return 0
    elif x == 2:
        return 1
    if x%2 == 0:
        return 0
    ir=int(x**(0.5))+1
    for i  in range(3,ir,2) :
        if x%i == 0:
            return 0
    return 1

n=int(input())

p=[]
for i in range(n+1):
    if isPrime(i):
        p.append([i,0])
        
for i in range(2,n+1):
    for j in range(len(p)):
        ii=i
        ip=0
        while ii>=p[j][0]:
            if ii%p[j][0]==0:
                ip=ip+1
                ii=ii//p[j][0]
            else:
                break
        p[j][1]=p[j][1]+ip

psum=1
for j in range(len(p)):
    if p[j][1]!=0:
        psum=mul(psum,p[j][1]+1)

print(psum)
        
