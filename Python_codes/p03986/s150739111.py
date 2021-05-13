import sys
from collections import deque
input = sys.stdin.readline


def main():
    X = input().rstrip()

    stack = deque()
    for s in X:
        if s == "S":
            stack.append(s)
        else:
            if len(stack) == 0 or stack[-1] == "T":
                stack.append(s)
            else:
                stack.pop()
    ans = len(stack)
    print(ans)


if __name__ == "__main__":
    main()
