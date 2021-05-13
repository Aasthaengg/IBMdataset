import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N = int(input().strip())
    P = [int(i) for i in input().strip().split()]

    ans = 0
    for i in range(len(P) - 1):
        if P[i] == i + 1:
            P[i + 1] = i + 1
            ans += 1
    if P[-1] == N:
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
