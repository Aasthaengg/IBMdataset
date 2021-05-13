def actual(N):
    for i in range(1, 10 ** 9 + 1):
        if i ** 2 > N:
            return (i - 1) ** 2

N = int(input())
print(actual(N))