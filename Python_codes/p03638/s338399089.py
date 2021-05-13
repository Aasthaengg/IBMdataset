def main():
    t = list(map(int, input().split()))
    mass = [[0]*t[1] for i in range(t[0])]
    input()
    colors = list(map(int, input().split()))

    w = 0
    h = 0
    direction = 0
    count = 0
    for color in colors:
        count += 1
        for i in range(color):
            mass[h][w] = count
            w = w + 1 if direction == 0 else w - 1
            if w == len(mass[0]) or w <= -1:
                h += 1
                direction = 1 if direction == 0 else 0
                w = 0 if direction == 0 else len(mass[0]) - 1
                continue
    for m in mass:
        print(' '.join([str(v) for v in m]))



if __name__ == '__main__':
    main()