n, x = map(int, input().split())
while not (n == 0 and x == 0):
    count = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            for c in range(b+1, n+1):
                if a + b + c == x:   
                    count = count + 1
    print(count)
    n, x = map(int, input().split())
