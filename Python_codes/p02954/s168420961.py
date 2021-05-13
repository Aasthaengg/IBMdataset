s = input()
n = len(s)
r_i = 0
odd, even = 0, 0
ans = [0] * n
for i in range(n):
    if i % 2 == 0: even += 1
    else: odd += 1
    if i == n - 1 or s[i] != s[i + 1]:
        if s[i] == 'R': r_i = i
        if r_i % 2 == 1: even, odd = odd, even
        ans[r_i] += even
        ans[r_i + 1] += odd
        odd, even = 0, 0
print(*ans, sep=' ')