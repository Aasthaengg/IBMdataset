import sys
while True:
    (n, x) = [int(i) for i in sys.stdin.readline().split()]
    if n == x == 0:
        break
    count = 0
    for i in range(1, n + 1):
        if i >= x: break
        for j in range(i + 1, n + 1):
            if i + j >= x: break
            for k in range(j + 1, n + 1):
                if i + j + k == x: count += 1
                elif i + j + k > x: break
    print(count)