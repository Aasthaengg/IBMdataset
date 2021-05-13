import sys
from bisect import bisect_left
def input(): return sys.stdin.readline().strip()

def main():
    A, B, Q = map(int, input().split())
    S = [-10**50]
    T = [-10**50]
    for _ in range(A): S.append(int(input()))
    for _ in range(B): T.append(int(input()))
    S.append(10**50)
    T.append(10**50)

    for _ in range(Q):
        x = int(input())
        idx1 = bisect_left(S, x)
        idx2 = bisect_left(T, x)
        ans = 10 ** 11
        cand1 = (x - S[idx1 - 1]) + abs(S[idx1 - 1] - T[idx2 - 1])
        ans = min(ans, cand1)
        cand2 = (x - S[idx1 - 1]) + (T[idx2] - S[idx1 - 1])
        ans = min(ans, cand2)
        cand3 = (S[idx1] - x) + (S[idx1] - T[idx2 - 1])
        ans = min(ans, cand3)
        cand4 = (S[idx1] - x) + abs(S[idx1] - T[idx2])
        ans = min(ans, cand4)
        cand5 = (x - T[idx2 - 1]) + abs(T[idx2 - 1] - S[idx1 - 1])
        ans = min(ans, cand5)
        cand6 = (x - T[idx2 - 1]) + (S[idx1] - T[idx2 - 1])
        ans = min(ans, cand6)
        cand7 = (T[idx2] - x) + (T[idx2] - S[idx1 - 1])
        ans = min(ans, cand7)
        cand8 = (T[idx2] - x) + abs(T[idx2] - S[idx1])
        ans = min(ans, cand8)
        print(ans)



if __name__ == "__main__":
    main()
