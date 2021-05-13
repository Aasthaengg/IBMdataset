def prime_factorize(N,lis):
    a = []
    n = N
    while n % 2 == 0:
        lis[2] += 1
        n //= 2
    f = 3
    while f * f <= N:
        if n % f == 0:
            lis[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        lis[n] += 1

N = int(input())
lis = [0] * 101
for i in range(1,N+1):
    prime_factorize(i,lis)
#print(lis)
lis.sort()
ans = 0
for i in range(101):
    for j in range(i+1,101):
        for k in range(j+1,101):
            if lis[i] >= 2 and lis[j] >= 4:
                ans += 1
            if lis[i] >= 4:
                ans += 2
for i in range(101):
    for j in range(i+1,101):
        if lis[i] >= 4 and lis[j] >= 14:
            ans += 1
            if lis[i] >= 14:
                ans += 1
        if lis[i] >= 2 and lis[j] >= 24:
            ans += 1
            if lis[i] >= 24:
                ans += 1
for i in range(101):
    if lis[i] >= 74:
        ans += 1
print(ans)
