n = int(input())
a = list(map(int, input().split()))

ans = 0
c = 0
while True:
    for i in range(n):
        if a[i] % 2 == 0:
            c += 1
    if c == n:
        for i in range(n):
            a[i] = a[i] // 2
        ans += 1
        c = 0
    else:
        print(ans)
        exit()
