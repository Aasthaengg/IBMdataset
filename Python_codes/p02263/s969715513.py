import sys

def main():
    expr = sys.stdin.readline().strip().split(' ')
    stack = []
    
    for i in expr:
        if i == '*' or i == '+' or i == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            ans = eval(n2 + i + n1)
            stack.append(str(ans))
        else:
            stack.append(i)

    print(stack.pop())
    
if __name__ == '__main__':
    main()