def main():
    N = int(input())
    H = list(map(int, input().split()))
    idx = 0
    mv = 0
    height = None
    vals = set([0])
    while True:
        height = H[idx]
        idx += 1
        if idx == N:
            if mv != 0:
                vals.add(mv)
            break
        if height >= H[idx]:
            mv += 1
        else:
            vals.add(mv)
            mv = 0
    print(max(list(vals)))


if __name__ == '__main__':
    main()
