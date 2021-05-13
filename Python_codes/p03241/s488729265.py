
def divisor(n):
    ass = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass  # sortされていない


n, m = map(int, input().split())
m_div = divisor(m)
m_div.sort()
ans = 0
for i in m_div:
    if i * n <= m and (m - i*n) % i == 0:
        ans = max(ans, i)
print(ans)