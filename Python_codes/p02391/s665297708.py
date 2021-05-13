if __name__ == '__main__':
    a, b = [int(i) for i in input().split()]
    symbol = None
    if a > b:
        symbol = '>'
    elif a < b:
        symbol = '<'
    else:
        symbol = '=='
    print("{0} {1} {2}".format('a', symbol, 'b'))