def resolve():
    A = sorted([int(i) for i in input().split()])
    if max(A) * 3 % 2 == sum(A) % 2:
        print((max(A) * 3 - sum(A)) // 2)
    else:
        print(((max(A) + 1) * 3 - sum(A)) // 2)


resolve()
