import sys

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))

    n_zero = x.count(0)
    if n_zero >= K:
        print(0)
        exit()
    
    K -= n_zero
    A = []  # < 0
    B = []  # > 0
    for _x in x:
        if _x < 0:
            A.append(-_x)
        elif _x > 0:
            B.append(_x)
    A = A[::-1][:K]
    B = B[:K]
    ans = float("INF")

    for n_A in reversed(range(len(A) + 1)):
        n_B = K - n_A
        if n_B > len(B):
            break

        if n_A == 0 and n_B == K:
            ans = min(ans, B[-1])
        elif n_A == K and n_B == 0:
            ans = min(ans, A[-1])
        else:
            a = A[n_A - 1]
            b = B[n_B - 1]
            time = a + b + min(a, b)
            ans = min(ans, time)

    print(ans)


if __name__ == "__main__":
    main()
