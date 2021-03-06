mod=10**9+7

def add(a, b):
    return (a + b) % mod

def sub(a, b):
    return (a + mod - b) % mod

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def div(a, b):
    return mul(a, power(b, mod-2))

def cc(ii):
    iii=1
    for ii in range(1,ii+1):
        iii=iii*ii
    return iii

def cmb(a,b):
    iii=1
    for ii in range(a-b+1,a+1):
        iii=(iii*ii)%mod
    iiii=1
    for ii in range(1,b+1):
        iiii=(iiii*ii)%mod
#        print("ii,iiii:",ii,iiii)
#    print("a:",a,"b:",b,"iii:",iii,"iiii:",iiii)
#    print("a:",a,"b:",b,"a-b:",a-b,"a!:",iii,"b!:",iiii,"cmb:",iii//iiii)
    return div(iii,iiii)        


n,k=map(int,input().split())

ib=k-1
ir=n-ib

for i in range(1,ib+2):
#    cb=cc(ib)//cc(ib-i+1)//cc(i-1)
#    cr=cc(ir)//cc(ir-i)//cc(i)
    cb=cmb(ib,i-1)
    cr=cmb(ir,i)
#    print("ib:",ib,i-1,cb,"ir:",ir,i,cr)
    print(mul(cb,cr))
    
