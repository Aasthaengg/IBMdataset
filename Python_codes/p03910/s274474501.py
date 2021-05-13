N = int(input())

s = 0
for i in range(1, N + 1):
    s += i
    if s >= N:
        tmp = i
        break

n = s - N

for i in range(1, n):
    print(i)

for i in range(n + 1, tmp + 1):
    print(i)
