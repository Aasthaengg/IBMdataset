# coding=utf-8

while True:
    height, width = map(int, raw_input().split())
    if height + width == 0:
        break
    else:
        outer = '#' * width + '\n'
        inner = '#' + '.' * (width -2) + '#\n'
        print outer + inner * (height - 2) + outer