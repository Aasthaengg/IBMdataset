def resolve():
    n = int(input())
    A = [int(input()) for i in range(n)]
    B = sorted(A)
    mx = B[-1]
    second = B[-2]
    for a in A:
        if a == mx:
            print(second)
        else:
            print(mx)
resolve()