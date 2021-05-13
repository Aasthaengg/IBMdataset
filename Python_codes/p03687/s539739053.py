import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    S = input().strip()

    ans = len(S)
    for i in range(len(S)):
        tmp = 0
        ma = 0
        for j in range(i + 1):
            if S[i] == S[j]:
                ma = max(ma, tmp)
                tmp = 0
            else:
                tmp += 1
        ans = min(ans, max(ma, len(S) - i - 1))

    print(ans)



if __name__ == '__main__':
    main()
