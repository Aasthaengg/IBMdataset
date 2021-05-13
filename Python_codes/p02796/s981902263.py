import sys
from operator import itemgetter

input = sys.stdin.readline


def main():
    N = int(input())
    LR = [None] * N
    for i in range(N):
        X, L = map(int, input().split())
        LR[i] = (X - L, X + L)

    LR.sort(key=itemgetter(0))
    ans = N
    cur_R = LR[0][1]
    for L, R in LR[1:]:
        if L < cur_R:
            ans -= 1
            if R < cur_R:
                cur_R = R
        else:
            cur_R = R

    print(ans)


if __name__ == "__main__":
    main()
