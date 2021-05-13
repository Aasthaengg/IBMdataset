n = int(input())

t = []

for i in range(n):
    t.append(int(input()))

buy = t[0]
val = t[-1] - buy

for i in range(1, n):
    if t[i] - buy > val:
        val = t[i] - buy
    if t[i] < buy:
        buy = t[i]

print(val)

