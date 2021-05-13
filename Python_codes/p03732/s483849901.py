# ABC060D - Simple Knapsack (ARC073D)
from itertools import accumulate as acc


def main():
    N, W, *A = map(int, open(0).read().split())
    V, x = [[] for _ in range(4)], A[0]  # x: w1 (W1 ≤ wi ≤ w1 + 3)
    for w, v in zip(*[iter(A)] * 2):  # group by weight
        V[w - x].append(v)
    for i in range(4):  # V[i][j] := max value of picking up j items from group i
        V[i] = tuple(acc([0] + sorted(V[i], reverse=1)))
    L = [len(v) for v in V]
    ans = 0
    for i in range(L[0]):
        for j in range(L[1]):
            for k in range(L[2]):
                w = i * x + j * (x + 1) + k * (x + 2)
                if w > W:
                    break
                l = min(L[3] - 1, (W - w) // (x + 3))
                v = V[0][i] + V[1][j] + V[2][k] + V[3][l]
                ans = max(ans, v)
    print(ans)


if __name__ == "__main__":
    main()