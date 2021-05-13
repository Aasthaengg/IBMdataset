for e in iter(input, '0 0'):
    h, w = map(int, e.split())
    print(('#' * w + '\n') * h)
