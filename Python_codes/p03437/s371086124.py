def main():
    X, Y = map(int, input().split())

    if X % Y == 0:
        print(-1)
    elif Y == 1:
        print(-1)
    else:
        print(X * (Y - 1))


main()