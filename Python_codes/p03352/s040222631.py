def resolve():
    X = int(input())
    ans = 1
    for b in range(1000 + 1, 1, -1):
        for p in range(2, 10 + 1):
            if b ** p <= X:
                ans = max(ans, b ** p)
    print(ans)


resolve()