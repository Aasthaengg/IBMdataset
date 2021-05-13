n = int(input())
D = sorted([int(i) for i in input().split()])

if n % 2 == 1:
    print(0)
else:
    m = n // 2
    print(D[m] - D[m - 1])