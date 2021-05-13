def main():
    a, b, c = (int(i) for i in input().split())
    for k in range(c):
        ap, bp = 0, 0
        if k % 2 == 0:
            if a % 2:
                a -= 1
            ap = a//2
            a = a//2
            b += ap
        else:
            if b % 2:
                b -= 1
            bp = b//2
            b = b//2
            a += bp
    print(a, b)


if __name__ == '__main__':
    main()
