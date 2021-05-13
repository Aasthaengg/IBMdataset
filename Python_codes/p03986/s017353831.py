def main():
    N = input().strip()
    stack = []
    for s in N:
        if len(stack)==0:
            stack.append(s)
        elif stack[-1]=="S" and s=="T":
            stack.pop()
        else:
            stack.append(s)
    print(len(stack))


if __name__ == "__main__":
    main()