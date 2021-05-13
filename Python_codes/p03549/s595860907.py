def main():
    N, M = (int(i) for i in input().split())
    t = (N-M)*100 + 1900*M
    print(t*2**M)


if __name__ == '__main__':
    main()
