def main():
    x, y = map(int, input().split())

    r = 1
    a = x
    while True:
        a *= 2
        if a <= y:
            r += 1
        else:
            break
    print(r)

if __name__ == '__main__':
    main()
