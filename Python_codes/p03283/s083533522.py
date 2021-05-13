
import numpy as np

def resolve():
    N, M, Q = map(int, input().split())
    L, R = np.array([list(map(int, input().split())) for _ in range(M)]).T
    P, Q = np.array([list(map(int, input().split())) for _ in range(Q)]).T
    P -= 1
    S = np.zeros(((N + 1), (N + 1)))

    # L,Rの区間にある本数
    np.add.at(S, (L,R), 1)

    # ゼータ変換（横縦累積和） axis=1:横, axis=0:縦
    S = np.cumsum(S, axis=1).cumsum(axis=0)

    ans = S[P, P] - S[P, Q] - S[Q, P] + S[Q, Q]
    print(*ans.astype(int), sep="\n")

if __name__ == "__main__":
    resolve()