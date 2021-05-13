import sys

input = lambda: sys.stdin.readline().rstrip()


def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    BC = [()] * M
    for i in range(M):
        b, c = map(int, input().split())
        BC[i] = (b, c)

    BC.sort(key=lambda x: x[1], reverse=True)

    am = []
    for bc in BC:
        b, c = bc[0], bc[1]
        if len(am) + b <= N:
            am += [c] * b
        else:
            am += [c] * (N - len(am))

        if len(am) == N:
            break

    A += am
    A.sort(reverse=True)
    ans = sum(A[:N])
    print(ans)


if __name__ == '__main__':
    solve()
