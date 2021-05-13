import sys
read = sys.stdin.read
def main():
    n, *a = map(int, read().split())
    r = 0
    for ea in a:
        while True:
            if ea % 2 == 0:
                r += 1
                ea //= 2
            else:
                break
    print(r)


if __name__ == '__main__':
    main()