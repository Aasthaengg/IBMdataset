n = int(input())

if n % 2 == 0:
    # 1 <-> n, 2 <-> n-1... is Pair
    print(int(n*(n-1)/2-n/2))
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i + j != n + 1:
                print(str(i) + " " + str(j))
else:
    # Each edge has (sum - N)
    print(int(n*(n-1)/2-(n-1)/2))
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i + j != n:
                print(str(i) + " " + str(j))
