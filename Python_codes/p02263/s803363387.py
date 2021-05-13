
def solve(tokens):
    stack = []

    for token in tokens:
        if token == "+":
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append(t1 + t2)
        elif token == "-":
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append(t2 - t1)
        elif token == "*":
            t1 = stack.pop()
            t2 = stack.pop()
            stack.append(t1 * t2)
        else:
            stack.append(int(token))

    return stack.pop()


def main():
    print solve(raw_input().split())


if __name__ == "__main__":
    main()