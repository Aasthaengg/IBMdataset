Fact=[1]
for i in range(1,50+1):
    Fact.append(Fact[-1]*i)

def nCr(n,r):
    return Fact[n]//(Fact[r]*Fact[n-r])
N,P=map(int,input().split())
A=list(map(int,input().split()))

Odd,Even=0,0
for a in A:
    if a%2:
        Odd+=1
    else:
        Even+=1

T=0
for r in range(P,Odd+1,2):
    T+=nCr(Odd,r)
print(T*(2**Even))
