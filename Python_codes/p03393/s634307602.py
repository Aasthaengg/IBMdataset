import sys
from string import ascii_lowercase as AL
input = sys.stdin.readline


def main():
    S = input().rstrip()

    if len(S) < 26:
        for a in AL:
            if a not in S:
                ans = S + a
                break
    else:
        i = 25
        while True:
            if i == 0:
                ans = -1
                break
            if S[i-1] > S[i]:
                i -= 1
            else:
                idx = AL.index(S[i-1])
                while True:
                    idx += 1
                    if AL[idx] in S[i:]:
                        next_al = AL[idx]
                        break
                ans = S[:i-1] + next_al
                break
    print(ans)


if __name__ == "__main__":
    main()
