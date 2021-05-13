N=int(input())
X=input()
def popcount(n):
    s=str(bin(n))
    return len([i for i in s if i=='1'])
def f(n):
    c=1
    while n!=0:
        n=n%popcount(n)
        c=c+1
    return c
x=int(X,2)
P=popcount(x)
F=list(X)
L=[1,2]# L[i]=2**i%(P+1)
M=[1,2]# M[i]=2**i%(P-1)
if P!=1:
    for i in range(1,N):
        L.append((L[i]*2)%(P+1))
        M.append((M[i]*2)%(P-1))
    s=x%(P+1)
    t=x%(P-1)
    for i in range(N):
        if F[i] == '1':
            q = (t - M[N-i-1])%(P-1)
            print(f(q))
        else:
            Q = P + 1
            q = (s + L[N-i-1])%(P+1)
            print(f(q))
else:
    for i in range(1,N):
        L.append(0)
    s=x%2
    for i in range(N):
        if F[i] == '1':
            print(0)
        else:
            q = (s + L[N - i - 1])%2
            print(f(q))