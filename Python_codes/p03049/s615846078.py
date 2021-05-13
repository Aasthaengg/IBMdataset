import sys

input = sys.stdin.readline


def main():
    N = int(input())
    S = [""] * N
    for i in range(N):
        S[i] = input().rstrip()

    xABx = 0
    xxxA = 0
    Bxxx = 0
    BxxA = 0
    for s in S:
        xABx += s.count("AB")
        if s[0] == "B" and s[-1] == "A":
            BxxA += 1
        elif s[0] == "B":
            Bxxx += 1
        elif s[-1] == "A":
            xxxA += 1

    if BxxA == 0:
        ans = xABx + min(xxxA, Bxxx)
    else:
        if xxxA == Bxxx == 0:
            ans = xABx + (BxxA - 1)
        else:
            ans = xABx + BxxA + min(xxxA, Bxxx)
    print(ans)


if __name__ == "__main__":
    main()
