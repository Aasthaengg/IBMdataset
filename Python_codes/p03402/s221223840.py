def main():
    A, B = map(int, input().split())

    white = [['.' for _ in [0] * 100] for _ in [0] * 50]
    black = [['#' for _ in [0] * 100] for _ in [0] * 50]
    paint(black, A)
    paint(white, B)

    print(100, 100)
    for wb in (white, black):
        for c in wb:
            print(*c, sep='')

def paint(color, n):
    if n == 1:
        return
    if color[0][0] == '.':
        char = '#'
    else:
        char = '.'
    for i in range(1, 50, 2):
        for j in range(1, 100, 2):
            color[i][j] = char
            n -= 1
            if n == 1:
                return

main()
