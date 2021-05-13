def divisor(i):
    s = []
    for j in range(1, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            s.append(i // j)
            s.append(j)
    return sorted(set(s))

n = int(input())
s = divisor(n)
ans = 0
for i in s:
    if n > i * (i + 1):
        ans += n // i - 1
print(ans)