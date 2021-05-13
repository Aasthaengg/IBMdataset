def main():
    _ = int(input())
    k = int(input())
    x = map(int, input().split())
    print(sum([min([abs(xi - point) for point in [0, k]]) * 2 for xi in x]))


if __name__ == '__main__':
    main()
