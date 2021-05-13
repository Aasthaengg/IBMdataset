def main():
    N = int(input())
    ab = [[int(i) for i in input().split()] for j in range(N)]
    ab.sort(key=lambda p: p[1])
    print(ab[0][0] + ab[0][1])


if __name__ == '__main__':
    main()
