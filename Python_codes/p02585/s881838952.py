from typing import List

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))


def solve(N: int, K: int, P: List[int], C: List[int]):
    ans = max(C)
    visited = [False] * N
    for i in range(N):
        if visited[i]:
            continue

        cycle = []
        to = i
        while not visited[to]:
            visited[to] = True
            cycle.append(C[to])
            to = P[to] - 1

        ans = max(ans, partial_solve(len(cycle), K, cycle))

    return ans


def partial_solve(N: int, K: int, A: List[int]):
    ret = max(A)
    B = [0] * (3 * N + 1)
    for i in range(1, 3 * N + 1):
        B[i] = B[i - 1] + A[(i - 1) % N]

    if N > K:
        for l in range(1, N + 1):
            for r in range(l, l + K):
                ret = max(ret, B[r] - B[l - 1])

    else:
        if B[N] < 0:
            K = N
            for l in range(1, N + 1):
                for r in range(l, l + K):
                    ret = max(ret, B[r] - B[l - 1])
        else:
            cnt = K // N - 1

            K = K % N + N

            for l in range(1, N + 1):
                for r in range(l, l + K):
                    ret = max(ret, B[r] - B[l - 1])

            ret += cnt * B[N]

    return ret

print(solve(N, K, P, C))
