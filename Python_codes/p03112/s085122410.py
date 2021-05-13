import sys
from bisect import bisect_left

def solve():
    input = sys.stdin.readline
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    Ans = [0] * Q
    for i in range(Q):
        x = int(input())
        si, ti = bisect_left(S, x), bisect_left(T, x)
        shortest_path = 10 ** 20
        if si < A and ti < B: shortest_path = min(shortest_path, max(S[si], T[ti]) - x)
        if si > 0 and ti > 0: shortest_path = min(shortest_path, x - min(S[si-1], T[ti-1]))
        if si > 0 and ti < B: shortest_path = min(shortest_path, T[ti] - S[si-1] + min(T[ti] - x, x - S[si-1]))
        if ti > 0 and si < A: shortest_path = min(shortest_path, S[si] - T[ti - 1] + min(S[si] - x, x - T[ti-1]))
        Ans[i] = shortest_path
    print("\n".join(map(str, Ans)))

    return 0

if __name__ == "__main__":
    solve()