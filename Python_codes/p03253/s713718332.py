import math
N,M = map(int,input().split())
mod = 10**9+7

if M == 1:
    print(1)
    exit()

m = M
A = []  #Mの素因数のリスト(今回は必要ない)
B = []  #各素因数で何回割り切れるか
for i in range(2,int(math.sqrt(M))+1):
    if m % i == 0:
        A.append(i)
        c = 0
        while m % i == 0:
            m = m // i
            c += 1
        B.append(c)

if m != 1:
    A.append(m)
    B.append(1)

def p(m,n):
    a = 1
    for i in range(n):
        a = a*(m-i) % mod
    return a

def c(m,n):
    return (p(m,n)*pow(p(n,n),mod-2,mod)) % mod

ans = 1
for i in range(len(B)):
    ans = (ans * c(N-1+B[i],B[i])) % mod

print(ans)