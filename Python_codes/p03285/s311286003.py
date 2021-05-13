N = int(input())
for i in range(100):
    for j in range(100):
        for h in range(100):
            if (4 * i) + (7 * j) + (11 * h) == N:
                print('Yes')
                exit()
print('No')