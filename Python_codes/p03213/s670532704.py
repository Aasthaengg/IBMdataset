n = int(input())
p = (n+1)*[0]

for i in range(2, n+1):
    now = i
    for j in range(2, i+1):
        while now % j == 0:
            p[j] += 1
            now //= j


def cnt(m):
    return len(list(filter(lambda x: x >= m, p)))


ans = 0
ans += cnt(74)
ans += cnt(24)*(cnt(2)-1)
ans += cnt(14)*(cnt(4)-1)
ans += cnt(4)*(cnt(4)-1)*(cnt(2)-2)//2
print(ans)
