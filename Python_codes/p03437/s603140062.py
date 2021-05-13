def main():
    X, Y = (int(i) for i in input().split())
    if X % Y == 0:
        print(-1)
    else:
        print(X)


if __name__ == '__main__':
    main()
