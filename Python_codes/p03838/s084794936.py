def main():
    import sys
    input = sys.stdin.readline
    x, y = [int(x) for x in input().strip().split()]
    dist = abs(abs(x) - abs(y))
    if x + dist == y:
        print(dist)
    elif - x + dist == y or - (x + dist) == y:
        print(dist + 1)
    elif - (- x + dist) == y:
        print(dist + 2)

if __name__ == '__main__':
    main()