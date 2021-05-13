import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()

    for s in "KIHBR":
        if S.count(s) != 1:
            print("NO")
            exit()

    A = S.count("A")
    if len(S) - A != 5:
        print("NO")
        exit()

    K = S.find("K")
    I = S.find("I")
    H = S.find("H")
    B = S.find("B")
    R = S.find("R")
    if not (K < I < H < B < R):
        print("NO")
        exit()
    if K > 1:
        print("NO")
        exit()
    if I - K != 1:
        print("NO")
        exit()
    if H - I != 1:
        print("NO")
        exit()
    if B - H > 2:
        print("NO")
        exit()
    if R - B > 2:
        print("NO")
        exit()
    if len(S) - 1 - R > 1:
        print("NO")
        exit()

    print("YES")


if __name__ == "__main__":
    main()
