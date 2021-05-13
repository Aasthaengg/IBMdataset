def resolve():
    A, B, K = [int(i) for i in input().split()]
    offset = 0
    while offset < K and A + offset <= B:
        print(A + offset)
        offset += 1
    begin = A + offset
    r = max(B - K + 1, begin)
    while r <= B:
        print(r)
        r += 1


resolve()
