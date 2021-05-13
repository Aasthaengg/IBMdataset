def main():
    X, t = (int(i) for i in input().split())
    print(max(X-t, 0))


if __name__ == '__main__':
    main()
