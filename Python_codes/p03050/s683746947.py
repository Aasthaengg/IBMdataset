def make_divisors(n):
    lw, up = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lw.append(i)
        if i * i != n:
            up.append(n//i)
        i += 1
    return lw + up[::-1]

N = int(input())
ans = 0
li = make_divisors(N)
if N == 1 or N==2:
    print(0)
    exit()

for x in li:
    if x * (x+2) > N:
        break
    ans += N//x - 1
print(ans)
