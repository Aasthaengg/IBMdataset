import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    X = input().strip()
    stack = list()
    for s in X:
        if s == "S" or len(stack) < 1:
            stack.append(s)
        elif s == "T" and stack[-1] == "T":
            stack.append(s)
        else:
            stack.pop()
    return len(stack)


if __name__ == "__main__":
    print(main())