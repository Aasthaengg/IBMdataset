import sys
from collections import deque

input = sys.stdin.readline


def dfs(N):
    alphabet = "abcdefghij"
    stack = deque(["a"])
    ans = []
    while stack:
        s = stack.pop()
        if len(s) == N:
            ans.append(s)
            continue
        for suffix in reversed(alphabet[:len(set(s)) + 1]):
            stack.append("".join((s, suffix)))
    return ans


def main():
    N = int(input())

    ans = dfs(N)
    print("\n".join(ans))


if __name__ == "__main__":
    main()
