def resolve():
    X = int(input())
    ans = []
    for p in range(2, 10):
        for b in range(1, 35):
            if b**p <= X:
                ans.append(b**p)
    print(max(ans))
resolve()