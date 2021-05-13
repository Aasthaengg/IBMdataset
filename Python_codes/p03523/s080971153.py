import sys
input = sys.stdin.readline


def main():
    S = input().strip()

    if S[0] != "A":
        S = "A" + S
    i = S.find("B")
    if i > -1 and S[i-1] != "A":
        S = S[:i] + "A" + S[i:]
    i = S.find("R")
    if i > -1 and S[i-1] != "A":
        S = S[:i] + "A" + S[i:]
    if S[-1] != "A":
        S = S + "A"

    if S == "AKIHABARA":
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
