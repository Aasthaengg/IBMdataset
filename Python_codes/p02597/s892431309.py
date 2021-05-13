#!/usr/bin/env python3


def solve(N, S):
    l = 0
    r = len(S) - 1
    answer = 0
    while l < r:
        if S[l] == "R":
            l += 1
        elif S[r] == "W":
            r -= 1
        else:
            # S[l] == 'W' S[r] == 'R' l < r
            l += 1
            r -= 1
            answer += 1

    return answer


def main():
    N = int(input())
    S = input()
    answer = solve(N, S)
    print(answer)


if __name__ == "__main__":
    main()
