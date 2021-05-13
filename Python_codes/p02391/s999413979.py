a, b = map(int, input().split(' '))
operator = '==' if a == b else '<' if a < b else '>' if a > b else ''
print('a %s b' % (operator))