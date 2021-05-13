import sys
from collections import deque

input = sys.stdin.readline


def main():
    S = input().rstrip()

    stack = deque()
    ans = 0
    for s in S:
        if len(stack) == 0:
            stack.append(s)
        else:
            if stack[-1] != s:
                stack.pop()
                ans += 2
            else:
                stack.append(s)

    print(ans)


if __name__ == "__main__":
    main()
