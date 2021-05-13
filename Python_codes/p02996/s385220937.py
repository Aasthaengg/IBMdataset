n = int(input())
tsk = []
for i in range(n):
    a, b = map(int, input().split())
    tsk.append((b, a))
tsk.sort()

t = 0
for i, (b, a) in enumerate(tsk):
    t += a
    if t > b:
        print('No')
        exit()
else:
    print('Yes')