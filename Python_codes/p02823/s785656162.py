
def resolve():
    N, A, B = list(map(int, input().split()))

    if abs(A-B) % 2 == 0:
        print((B - A) //2)
    else:
        print(min(A, N-B+1) + (B -A -1) // 2)
    return

resolve()