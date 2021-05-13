#エラトネスの篩
def Eratosthene(n):
    prime = [1]*(n+1)
    prime[0] = 0
    prime[1] = 0

    for i in range(2, int(n**0.5)+1, 1):
        if prime[i]==0:
            continue
        for j in range(i+1, n+1, 1):
            if prime[j]==0:
                continue
            if j%i==0:
                prime[j] = 0
    return prime

prime = Eratosthene(10**3)
P = []
for i in range(10**3+1):
    if prime[i]==1:
        P.append(i)

N = int(input())

ANS = 1
for p in P:
    a = p
    ans = 0
    while 1:
        if N/p>0:
            ans = ans + int(N/p)
        else:
            break
        p = p*a
    ANS = ANS * (ans+1)
print(ANS%(10**9+7))