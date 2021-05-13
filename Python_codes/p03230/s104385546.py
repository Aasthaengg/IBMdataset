N = int(input())

size = 1
while True:
    n = size * (size-1) // 2
    if n == N:
        break
    elif n > N:
        print('No')
        exit()
    size += 1

sets = [[] for _ in range(size)]

n = 1
for i in range(size):
    for j in range(i+1, size):
        sets[i].append(n)
        sets[j].append(n)
        n += 1

print('Yes')
print(size)
for i in range(size):
    print(' '.join(map(str, [len(sets[i])] + sets[i])))