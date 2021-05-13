
import numpy as np

def resolve():
    N, M, Q = map(int, input().split())
    S = np.zeros(((N + 1), (N + 1)))
    for _ in range(M):
        l, r = map(int, input().split())
        # L,Rの区間にある本数
        S[l, r] += 1

    # ゼータ変換（横縦累積和） axis=1:横, axis=0:縦
    S = np.cumsum(S, axis=1).cumsum(axis=0)

    for _ in range(Q):
        ans = 0
        l, r = map(int, input().split())
        l -= 1
        ans = S[r, r] - S[l, r] - S[r, l] + S[l, l]
        print(int(ans))


if __name__ == "__main__":
    resolve()