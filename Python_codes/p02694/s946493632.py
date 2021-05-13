X = int(input())
n = 100
for i in range(1, 10**9):
    n += n // 100
    if n >= X:
        print(i)
        exit()