n = int(input())
if n == 1:
    print(0)
    exit()

def primes(n):
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            prime[j] = False
    return [i for i in range(n + 1) if prime[i]]


pms = primes(n)
num = [0]*len(pms)
ans = 0
for j in range(2,n+1):
    for i in range(len(pms)):
        while j % pms[i] == 0:
            j //= pms[i]
            num[i] += 1
c74 = 0
c24 = 0
c14 = 0
c4 = 0
c2 = 0
for i in range(len(num)):
    if num[i] >= 74:
        c74 += 1
        c24 += 1
        c14 += 1
        c4 += 1
        c2 += 1
    elif num[i] >= 24:
        c24 += 1
        c14 += 1
        c4 += 1
        c2 += 1
    elif num[i] >= 14:
        c14 += 1
        c4 += 1
        c2 += 1
    elif num[i] >=4:
        c4 += 1
        c2 += 1
    elif num[i] >= 2:
        c2 += 1
ans += c74
ans += c24 * (c2-1)
ans += c14 * (c4-1)
ans += c4*(c4-1)//2 * (c2-2)
print(ans)






