def main():
    N,M = map(int,input().split())
    if N == 1 or M == 1:
        if N == M:
            print(1)
        else:
            print(N*M-2)
    else:
        print(N*M-2*(N+M-2))

if __name__ == '__main__':
    main()