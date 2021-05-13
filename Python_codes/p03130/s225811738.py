def resolve():
    a = []
    b = []
    for i in range(3):
        A, B = map(int, input().split())
        a.append(A)
        a.append(B)
    for j in range(1, 5):
        b.append(a.count(j))
    if b.count(2) == 2 and b.count(1) == 2:
        print("YES")
    else:
        print("NO")
resolve()