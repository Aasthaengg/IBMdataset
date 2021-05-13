s = input()
n = len(s)

a = [0] * (n + 1)

for i in range(n):
    if s[i] == '<':
        a[i + 1] = max(a[i + 1], a[i] + 1)
for i in range(n - 1, -1, -1):
    if s[i] == '>':
        a[i] = max(a[i], a[i + 1] + 1)

print(sum(a))
