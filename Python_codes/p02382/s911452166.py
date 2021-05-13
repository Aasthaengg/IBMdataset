def p(t):
    print(f'{t:.6f}')

n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

D1=0
D2=0
D3=0
D4=0

for i in range(n):
    d=x[i]-y[i]
    if d<0:
        d=-d
    
    D1+=d
    D2+=d**2
    D3+=d**3
    if d>D4:
        D4=d
        
p(D1)
p(D2**(1/2))
p(D3**(1/3))
p(D4)
