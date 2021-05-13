p = 10**9+7
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*(pow(x,(m-1)//2)**2)%p)%p
N,M = map(int,input().split())
A = [1 for _ in range(N+100)]
for i in range(2,N+100):
    A[i] = (A[i-1]*i)%p
B = [1 for _ in range(N+100)]
B[N+100-1] = pow(A[N+100-1],p-2)
for i in range(N+100-2,1,-1):
    B[i] = (B[i+1]*(i+1))%p
P = [1 for _ in range(10**5)]
P[0]=0
P[1]=0
for i in range(2,int((10**5)**0.5)+1):
    for j in range(i*i,10**5,i):
        P[j] = 0
Q = []
for i in range(2,10**5):
    if P[i]==1:
        Q.append(i)

C = {q:0 for q in Q}
for q in Q:
    if M%q==0:
        while M%q==0:
            M = M//q
            C[q] += 1
if M>1:
    C[M] = 1
    Q.append(M)
prod = 1
for q in Q:
    k = C[q]
    a = A[k+N-1]
    a = (a*B[N-1])%p
    a = (a*B[k])%p
    prod = (prod*a)%p
print(prod)