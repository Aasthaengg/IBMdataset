#!/usr/bin/env python3
def main():
    N, M = map(int, input().split())
    pS = [list(input().split()) for _ in range(M)]

    score = [0] * (N + 1)
    ac = [False] * (N + 1)
    for p, S in pS:
        res = int(p)
        if S == 'AC':
            ac[res] = True
        if ac[res]:
            continue
        score[res] += 1
    penalty = 0
    for i in range(N + 1):
        if ac[i]:
            penalty += score[i]
    print(sum(ac), penalty)
    # print(ac)
    # print(score)


if __name__ == '__main__':
    main()
