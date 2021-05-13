def main():
    n, m, c = map(int, input().split())
    blis = list(map(int, input().split()))
    alis = []
    for i in range(n):
        ilis = list(map(int, input().split()))
        alis.append(ilis)
    ans = 0
    for i in range(n):
        tmp = c
        for k in range(m):
            #print(alis, alis[i], alis[i][k], blis, blis[k])
            tmp += alis[i][k] * blis[k]
        if tmp > 0:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
