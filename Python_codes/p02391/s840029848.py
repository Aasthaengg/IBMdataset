a, b = [int(temp) for temp in input().split()]
op   = '==' if a == b else '<' if a < b else '>'
print('{} {} {}'.format('a',op,'b'))