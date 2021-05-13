def resolve():
    A, B, C = [int(i) for i in input().split()]
    for i in range(0, A * B + 1, A):
        if i % B == C:
            print("YES")
            return
    print("NO")


resolve()
