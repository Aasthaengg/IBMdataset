def stack(A):
    stack = []
    for opr in A:
        if opr.isdigit():
            stack.append(opr)
        else:
            opr1 = stack.pop()
            opr2 = stack.pop()
            stack.append(str(eval(opr2 + opr + opr1)))
    print stack.pop()

if __name__ == "__main__":
    A = raw_input().split()
    stack(A)