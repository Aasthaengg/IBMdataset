while True:
    n, x = [int(s) for s in input().split()]
    if n == x == 0:
        break
    
    total = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                st = i + j + k
                if x < st:
                    break
                if st == x:
                    total += 1
    print(total)