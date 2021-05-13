def main():
    sand_weight, time = map(int, input().split())
    print(sand_weight - time if sand_weight >= time else 0)


if __name__ == '__main__':
    main()

