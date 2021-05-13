N,M=map(int, input().split())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
n = 2*10 ** 5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p) 階乗のmod
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, n + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

# *////**//
F = factorization(M)

if N==1:
    print(1)
    exit()
if M==1:
    print(1)
    exit()
ans=1
for l in F:
    ans*=cmb(N-1+l[1], l[1], p)
    ans%=p

print(ans)