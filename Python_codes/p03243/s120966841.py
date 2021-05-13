n = int(input())
for i in range(n, n + 112):
    i = str(i)
    for j in range(1, 10):
        j = str(j)
        if i.count(j) == len(i):
            print(i)
            exit()