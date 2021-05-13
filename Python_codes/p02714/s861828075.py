n = int(input())
s = list(input())
r = 0
g = 0
b = 0


for i in range(n):
    if s[i] == 'R':
        r += 1
    elif s[i] == 'G':
        g += 1
    else:
        b += 1

ans = r * g * b

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        k = 2 * j - i
        if k < n:
            if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                ans -= 1


print(ans)
