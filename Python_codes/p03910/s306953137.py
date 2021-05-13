N = int(input())

for k in range(0, 10 ** 7):
    if k * (k + 1) // 2 < N <= (k + 1) * (k + 2) // 2:
        break
remove = (k + 1) * (k + 2) // 2 - N
for i in range(1, k + 2):
    if i != remove:
        print(i)


