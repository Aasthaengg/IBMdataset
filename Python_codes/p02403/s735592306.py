while True:
    h, w = map(int, input().split())
    if not h and not w:
        break
    print('\n'.join(['#' * w for x in range(h)]) + '\n')