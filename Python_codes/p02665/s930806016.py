n = int(input())
a = list(map(int, input().split()))

if a[0] != 0:
    if n == 0 and a[0] == 1:
        print(1)
    else:
        print(-1)
    exit()

ruiseki = a[::-1]
for i in range(1, n+1):
    ruiseki[i] += ruiseki[i-1]
ruiseki = ruiseki[::-1]

node = [1]
komoti = [1]
for i in range(1, n+1):
    ai = a[i]
    if komoti[-1]*2 >= ai:
        node.append(min(ruiseki[i], komoti[-1]*2))
        komoti.append(node[-1]-ai)
    else:
        print(-1)
        exit()

print(sum(node))