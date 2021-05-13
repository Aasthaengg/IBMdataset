import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    if A[0] == 0:
        answer = []
        for a in (1, -1):
            cnt = 1
            S = a
            for i in range(1, N):
                s = S + A[i]
                if A[i] == 0:
                    if S > 0:
                        cnt += S + 1
                        S = -1
                    else:
                        cnt += abs(S) + 1
                        S = 1
                else:
                    if s == 0:
                        if S < 0:
                            cnt += 1
                            S = 1
                        else:
                            cnt += 1
                            S = -1
                    else:
                        if S * s > 0:
                            if S < 0:
                                cnt += abs(s) + 1
                                S = 1
                            else:
                                cnt += s + 1
                                S = -1
                        else:
                            S = s
            answer.append(cnt)
        print(min(answer))
    else:
        if A[0] > 0:
            cnt1 = 0
            S1 = A[0]
            cnt2 = A[0] + 1
            S2 = -1
        else:
            cnt1 = 0
            S1 = A[0]
            cnt2 = abs(A[0]) + 1
            S2 = 1
        answer = []
        for cnt, S in [(cnt1, S1), (cnt2, S2)]:
            for i in range(1, N):
                s = S + A[i]
                if A[i] == 0:
                    if S > 0:
                        cnt += S + 1
                        S = -1
                    else:
                        cnt += abs(S) + 1
                        S = 1
                else:
                    if s == 0:
                        if S < 0:
                            cnt += 1
                            S = 1
                        else:
                            cnt += 1
                            S = -1
                    else:
                        if S * s > 0:
                            if S < 0:
                                cnt += abs(s) + 1
                                S = 1
                            else:
                                cnt += s + 1
                                S = -1
                        else:
                            S = s
            answer.append(cnt)
        print(min(answer))


if __name__ == "__main__":
    main()
