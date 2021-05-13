def resolve():
    n, a, b = map(int, input().split())
    
    ans = 0
    for i in range(n, 0, -1):
        snum = str(i)
        total = 0
        for c in snum:
            total += int(c)
        if a <= total and total <= b:
            ans += i
    print(ans)
resolve()