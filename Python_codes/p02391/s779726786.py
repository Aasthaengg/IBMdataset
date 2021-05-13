def expression(a, b):
    if a < b:
        return '<'

    if a > b:
        return '>'

    return '=='

a, b = map(int, input().split(' '))

print('a '+expression(a, b)+' b')