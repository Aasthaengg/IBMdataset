import sys
input = sys.stdin.readline


def main():
    n = int(input())
    ans = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            m = n if n & 1 else n + 1
            if i + j != m:
                ans.append((i, j))
    print(len(ans))
    for i, j in ans:
        print(i, j)


if __name__ == '__main__':
    main()
