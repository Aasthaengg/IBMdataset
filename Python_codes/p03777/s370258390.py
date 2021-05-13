atcodeer, topcodeer = map(str, input().split())

if atcodeer == 'H' and topcodeer == 'H':
    print('H')
elif atcodeer == 'H' and topcodeer == 'D':
    print('D')
elif atcodeer == 'D' and topcodeer == 'H':
    print('D')
elif atcodeer == 'D' and topcodeer == 'D':
    print('H')