stack = []
top = -1

def push(x):
    global stack
    global top

    top += 1
    stack.append(x)

def pop2():
    global top
    global stack

    top -= 1
    stack.pop()

def main():
    global top
    global stack

    S = input()
    ans = 0

    for i in range(len(S)):
        if i == 0:
            push(S[0])
            continue

        push(S[i])
        if stack[top] != stack[top-1]:
            pop2()
            pop2()
            ans += 2
            continue

    return ans

print(main())
