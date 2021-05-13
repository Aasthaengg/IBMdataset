n = int(input())
mod = 10**9 + 7

if n == 1:
    print(1)
    exit()
if n == 2:
    print(2)
    exit()

prime = [2]
for i in range(3, n+1):
    j = 0
    flag = True
    while prime[j] * prime[j] <= i:
        if i % prime[j] == 0:
            flag = False
            break
        j += 1
    if flag:
        prime.append(i)

ans = 1
for p in prime:
    num = 1
    i = p
    while i <= n:
        num += n // i
        i *= p
    ans *= num
    ans %= mod

print(ans)