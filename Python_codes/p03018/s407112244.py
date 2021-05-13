import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()

    lS = list(S)
    acnt = 0
    ans = 0
    for i in range(len(S) - 2):
        if lS[i] == "A":
            acnt += 1
        else:
            acnt = 0

        if lS[i] == "A" and lS[i + 1] == "B" and lS[i + 2] == "C":
            ans += acnt
            lS[i + 2] = "A"
            if acnt > 1:
                lS[i + 1] = "A"
                acnt -= 2

    print(ans)



if __name__ == '__main__':
    main()
