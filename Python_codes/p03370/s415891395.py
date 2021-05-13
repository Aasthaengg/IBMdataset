# ABC095 B

def main():
    n, x = map(int, input().split())
    M = [int(input()) for _ in range(n)]

    print((x - sum(M))//min(M) + n)

if __name__ == '__main__':
    main()