s = input()
n = len(s)
r, l = 0, 0
odd, even = 0, 0
ans = [0] * n
for i in range(n):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
    if i == n - 1 or s[i] != s[i + 1]:
        if s[i] == 'R':
            r, l = i, i + 1
        if r % 2 == 0:
            ans[r] += even
            ans[l] += odd
        else:
            ans[r] += odd
            ans[l] += even
        odd, even = 0, 0
print(*ans, sep=' ')