n = int(input())

def calc_sum(b, e):
    cnt = (e - b) // b + 1
    return (b + e) * cnt // 2

ans = 0
for i in range(1, n+1):
    ans += calc_sum(i, n // i * i)

print(ans)