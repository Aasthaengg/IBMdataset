N = int(input())

for i in range(N):
    for j in range(N - i):
        if 4 * i + 7 * j == N:
            print('Yes')
            exit()
print('No')