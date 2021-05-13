def main():
    N, K = map(int, input().split())
    H = map(int, input().split())
    print(len([h for h in H if h >= K]))


if __name__ == '__main__':
    main()
