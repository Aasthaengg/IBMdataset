Q = int(input())
Pr = [0]*(10**5+1)
Ta = [0]*(10**5+1)
Tb = [0]*(10**5+1)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

for k in range(10**5+1):
    s = 10**5-k
    if s%2==1:
        if Pr[s]==1:
            continue
        div = make_divisors(s)
        if len(div)==2:
            Pr[s]=1
        div = make_divisors((s+1)//2)
        if len(div)==2:
            Pr[(s+1)//2]=1

for k in range(10**5+1):
    if Pr[k]==1 and Pr[(k+1)//2]==1:
        Ta[k]=1

Tb[1]=0
for k in range(3,10**5+1):
    Tb[k]=Ta[k]+Tb[k-2]

for i in range(Q):
    L,R = list(map(int,input().split()))
    if L==1:
        X = 0
    else:
        X = Tb[L-2]
    Y = Tb[R]
    print(Y-X)