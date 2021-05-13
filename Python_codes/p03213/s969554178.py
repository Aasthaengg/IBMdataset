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
d = [0] * 100
for i in lis:
    d[i] += 1
for i in reversed(range(len(d)-1)):
    d[i] += d[i+1]

print(d[74] + d[24] * (d[2]-1) + d[14] * (d[4]-1) + (d[4] * (d[4]-1) * (d[2]-2)) // 2)
