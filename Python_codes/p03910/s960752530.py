N = int(input())

x = 0
for i in range(1, N+1):
    x += i
    if x >= N:
        j = i
        break

y = x-N

for i in range(1, j+1):
    if i == y:
        continue
    print(i)