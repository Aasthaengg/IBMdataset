import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N = int(input().strip())
    ans = set()
    for _ in range(N):
        A = int(input().strip())
        if A in ans:
            ans.remove(A)
        else:
            ans.add(A)

    return len(ans)


if __name__ == "__main__":
    print(main())
