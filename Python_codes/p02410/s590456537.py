def main():
    n, m = map(int, input().split())
    
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))

    b = []
    for _ in range(m):
        b.append(int(input()))

    for x in range(n):
        ans = 0
        for y in range(m):
            hoge = A[x][y] * b[y]
            ans += hoge
        print(ans)

if __name__ == "__main__":
    main()