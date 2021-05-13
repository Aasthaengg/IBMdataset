N = int(input())
count = {}
for i in range(2,N+1):
    f = 2
    tmp = i
    while f**2<=tmp:
        if tmp%f == 0:
            if f not in count:
                count[f] = 0
            count[f] += 1
            tmp //= f
        else:
            f += 1
    if tmp != 1:
        if tmp not in count:
            count[tmp] = 0
        count[tmp] += 1
ans = 1
for v in count.values():
    ans *= (v+1)

mod = 10**9 +7
print(ans%mod)

