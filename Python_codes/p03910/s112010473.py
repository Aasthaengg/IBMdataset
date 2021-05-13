n = int(input())
s = 0
i = 1
while s <= n:
    s += i
    i += 1
for j in range(1, i):
    if j == s - n:
        continue
    else:
        print(j)
