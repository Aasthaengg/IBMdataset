def main():
    h, w, k = map(int, input().split())
    c = []
    for i in range(h):
        c.append(list(input()))

    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            count = 0
            for ii in range(h):
                for jj in range(w):
                    if not (i >> ii & 1 or j >> jj & 1) and c[ii][jj] == "#":
                        count += 1
            if count == k:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
