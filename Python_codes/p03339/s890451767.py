n = int(input())
s = input()
e = [0] * n
w = [0] * (n + 1)
if s[0] == 'E':
        e[0] = 1
else:
        e[0] = 0
w[0] = 0
if s[0] == 'W':
        w[1] = 1
else:
        w[1] = 0
for i in range(1, n):
    if s[i] == 'E':
        e[i] = e[i - 1] + 1
        w[i + 1] = w[i]
    else:
        e[i] = e[i - 1]
        w[i + 1] = w[i] + 1
min = float("inf")
for i in range(n):
    if min > e[-1] - e[i] + w[i]:
        min = e[-1] - e[i] + w[i]
print(min)