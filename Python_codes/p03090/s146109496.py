n = int(input())

if n % 2 == 0:
    print(int(n * (n - 2) / 2))
    for i in range(1, n):
        for j in range(i, n + 1):
            if i + j != n + 1 and i != j:
                print(str(i) + " " + str(j))

else:
    print(int((n - 1) * (n - 1) / 2))
    for i in range(1, n-1):
        for j in range(i, n):
            if i + j != n and i != j:
                print(str(i) + " " + str(j))
    for k in range(1, n):
        print(str(k) + " " + str(n))