def main():
    n, m = map(int, input().split())
    ks = []
    for _ in range(m):
        ks.append(list(map(int, input().split())))
    p = list(map(int, input().split()))

    ans = 0
    for i in range(2**n):
        ls = [0]*m
        for j in range(n):
            if i & (1 << j):
                for k in range(m):
                    if j+1 in ks[k][1:]:
                        ls[k] += 1
        cnt = 0
        for l in range(m):
            if ls[l] % 2 == p[l]:
                cnt += 1
        if cnt == m:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
