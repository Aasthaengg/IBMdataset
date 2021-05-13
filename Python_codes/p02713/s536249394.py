def calc(a, b):
    m = min(a, b)
    l = max(a, b)
    while m != 0:
        s = m
        m = l % m
        l = s
    return l

K = int(input())
ans = 0
for i in range(K):
    for j in range(i+1):
        for k in range(j+1):
            if i == j == k:
                ans += i+1
            elif i == j:
                ans += 3 * calc(i+1, k+1)
            elif j == k:
                ans += 3 * calc(i+1, j+1)
            else:
                ans += 6 * calc(calc(i+1, j+1), k+1)

print(ans)