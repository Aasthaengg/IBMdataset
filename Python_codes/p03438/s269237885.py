def petrozavodsk001_b():
    _ = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    act = sum(B) - sum(A)
    if act < 0:
        print('No')
        return

    addA, addB = 0, 0
    for a, b in zip(A, B):
        if a > b: addB += a - b
        else: addA += (b - a + 1) // 2

    if addA <= act and addB <= act:
        print('Yes')
    else:
        print('No')

petrozavodsk001_b()