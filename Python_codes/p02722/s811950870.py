def divisors(n):
    lst = []; i = 1
    while i * i <= n:
        q, r = divmod(n, i)
        if r == 0:
            lst.append(i)
            if i != q: lst.append(q)
        i += 1
    return lst

N = int(input())
ans = len(divisors(N-1)) - 1
divs = divisors(N)
for k in divs:
    if k == 1: continue
    temp = N
    while temp % k == 0: temp //= k
    if temp % k == 1: ans += 1
print(ans)