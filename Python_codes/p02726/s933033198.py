def main():
    n, x, y = (int(i) for i in input().split())

    x -= 1
    y -= 1
    # assume vertices are numbered [0, n)

    cts = [0] * n
    for i in range(n):
        for j in range(i+1,n):
            dist = min(j-i, abs(x-i) + 1 + abs(y-j),
                    abs(i-y) + 1 + abs(x-j))
            cts[dist] += 1

    for i in range(1, n):
        print(cts[i])
main()
