k = int(input())

i = 0

ans = []

def rec(n):
    ans.append(n)
    if n >= 10000000000:
        return
    for j in range(-1, 2, 1):
        add = n % 10 + j
        if 0 <= add <= 9:
            rec(10 * n + add)
for i in range(1, 10):
    rec(i)
ans.sort()
print(ans[k - 1])
