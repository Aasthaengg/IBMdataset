def div(n):
    l = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            l.append(i)
            if i != n // i:
                l.append(n // i)
    return l
n = int(input())
l = div(n)
ans = 0
for i in l:
    if i - 1 != 0 and n // (i - 1) == n % (i - 1):
        ans += i - 1
print(ans)