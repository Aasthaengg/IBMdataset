from collections import deque


def main():
    word = input()
    stack = deque()
    for w in word:
        if w == "S":
            stack.appendleft(w)
        elif w == "T" and (len(stack) == 0 or stack[0] == "T"):
            stack.appendleft(w)
        else:
            stack.popleft()
    print(len(stack))


if __name__ == '__main__':
    main()

