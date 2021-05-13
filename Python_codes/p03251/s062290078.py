def main():
    N, M, X, Y = map(int, input().split())
    max_x = max(list(map(int, input().split())))
    min_y = min(list(map(int, input().split())))

    for z in range(X + 1, Y + 1):
        if max_x < z <= min_y:
            print("No War")
            exit()
    print("War")


if __name__ == '__main__':
    main()
