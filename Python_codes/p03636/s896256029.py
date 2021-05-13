def actual(s):
    head = s[0]
    tail = s[-1]
    length = len(s[1:-1])

    return f'{head}{length}{tail}'

s = input()
print(actual(s))