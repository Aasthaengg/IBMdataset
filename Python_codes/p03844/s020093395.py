if __name__ == '__main__':
    # A op B
    exp = input()
    a, op, b = exp.split(' ')
    a = int(a)
    b = int(b)
    
    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b

    print(ans)