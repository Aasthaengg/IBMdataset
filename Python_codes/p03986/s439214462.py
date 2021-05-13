import sys
from collections import deque

input = sys.stdin.readline


def main():
    X = input().rstrip()

    stack = deque()
    for x in X:
        if len(stack) == 0:
            stack.append(x)
        else:
            if x == "S":
                stack.append(x)
            else:
                if stack[-1] == "S":
                    stack.pop()
                else:
                    stack.append(x)
    ans = len(stack)

    print(ans)


if __name__ == "__main__":
    main()
