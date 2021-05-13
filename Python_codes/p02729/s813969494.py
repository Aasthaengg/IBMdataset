def main():
    N, M = map(int, input().split())

    e = N*(N-1)/2
    o = M*(M-1)/2

    ans = int(e + o)
    print(ans)


if __name__ == '__main__':
    main()