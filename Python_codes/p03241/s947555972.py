def divisors(n):
    res = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res

n, m = map(int, input().split())
ans = 0
nums = divisors(m)
nums.sort()
num = nums.pop(0)
while num * n <= m:
    if (m - num * n) % num == 0:
        ans = num
    if nums == []:
        break
    num = nums.pop(0)
print(ans)