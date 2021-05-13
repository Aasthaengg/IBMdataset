# FOLLOW ANSWER
N,C = map(int,input().split())

x = [0]
v = [0]

acc = [0]
rev = [0]
s = 0
res = 0
for i in range(N):
    a,b = map(int,input().split())
    x.append(a)
    v.append(b)
    s += b
    acc.append(s)


#OB < OA
#O->B->A = 2*OB + OA
F =  []

for i in range(N+1):
    F.append(acc[i]-x[i])
for i in range(1,N+1):
    F[i] = max(F[i],F[i-1])
for B in range(N+1):
    if B == 0:
        A = N
        costB = 0
    else:
        A = B - 1
        costB = (s-acc[B]+v[B]-2*(C-x[B]))
    
    res = max(res,F[A] + costB)

#OA < OB
#O->A->B = 2*OA + OB
F[0] = 0
for i in range(N,0,-1):
    F[i] = (s-acc[i]+v[i]-(C-x[i]))
    F[i] = max(F[i],F[(i+1)%(N+1)])
for A in range(N+1):
    if A == N:
        B = 0
    else:
        B = A + 1
    
    res = max(res,F[B] + acc[A]-2*x[A])
print(res) 
