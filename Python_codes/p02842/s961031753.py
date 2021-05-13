N = int(input())
n = int(N // 1.08)

while n <= N:
    if int(n * 1.08) == N:
        print(n)
        exit()

    n += 1

print(':(')
