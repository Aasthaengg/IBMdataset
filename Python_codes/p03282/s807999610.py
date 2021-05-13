import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()
    K = int(input())

    ans = 1
    for k in range(K):
        if S[k] != "1":
            ans = int(S[k])
            break

    print(ans)


if __name__ == "__main__":
    main()
