n,m = map(int, input().split())
X = [int(x) for x in input().split()]
Y = [int(y) for y in input().split()]
mod = 10**9+7

Xd = []
for i in range(n-1):
    Xd.append(X[i+1]-X[i])
    
Yd = []
for i in range(m-1):
    Yd.append(Y[i+1]-Y[i])
    
if n > 2:
    Xd[1] = 2*Xd[0] + 2*Xd[1]
    for i in range(n-3):
        Xd[i+2] = 2*Xd[i+1] - Xd[i] + (i+3)*Xd[i+2]
        Xd[i+2] %= mod
        
if m > 2:
    Yd[1] = 2*Yd[0] + 2*Yd[1]
    for i in range(m-3):
        Yd[i+2] = 2*Yd[i+1] - Yd[i] + (i+3)*Yd[i+2]
        Yd[i+2] %= mod
    
print(Xd[-1]*Yd[-1]%mod)