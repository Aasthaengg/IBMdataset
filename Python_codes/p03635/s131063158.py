def main():
    east_west, north_south = map(int, input().split())
    print((east_west - 1) * (north_south - 1))


if __name__ == '__main__':
    main()

