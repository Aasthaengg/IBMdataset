N = int(input())

tasks = []

for _ in range(N):
    a, b = map(int, input().split(' '))
    tasks.append((b, a))

tasks.sort()

t = 0
for b, a in tasks:
    t += a
    if t > b:
        print('No')
        break
else:
    print('Yes')
