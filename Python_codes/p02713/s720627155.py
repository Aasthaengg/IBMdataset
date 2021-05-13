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
    for j in range(K):
        for k in range(K):
            ans += calc(calc(i+1, j+1), k+1)

print(ans)