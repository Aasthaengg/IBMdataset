
def resolve():
    N = int(input())

    P = []
    for _ in range(N):
        x, l = map(int, input().split())
        P.append((x - l, x + l))

    P.sort(key=lambda x: x[1])

    cnt = 0
    pre = -(1 << 60)
    for (l, r) in P:
        if pre > l:
            continue
        cnt += 1
        pre = r

    print(cnt)


if __name__ == "__main__":
    resolve()