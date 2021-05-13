
def check(B, C):
    A = list(map(int, input().split()))
    s = 0
    for i, a in enumerate(A):
        s += a * B[i]
    s += C
    if s > 0:
        return True
    else:
        return False


def resolve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))

    ans = 0
    for _ in range(N):
        if check(B, C):
            ans += 1
    print(ans)
resolve()