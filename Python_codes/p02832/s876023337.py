def resolve():
    n = int(input())
    x = 0
    c = 0
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] == x+1:
            x += 1
            continue
        else:
            c += 1
    if c == n:
        print(-1)
    else:
        print(c)
resolve()