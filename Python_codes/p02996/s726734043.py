def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    t = 0
    for a, b in sorted(AB, key=lambda x: x[1]):
        t += a
        if t > b:
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    main()
