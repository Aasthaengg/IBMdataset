def theater():
    total = 0
    try:
        N = int(input())
        l_r = (list(map(lambda x: int(x), input().split(' '))) for elem in range(N))
    except:
        return
    if not (1 <= N and N <= 1000): return
    for l, r in l_r:
        if 1 <= l and l <= 100000 or 1 <= r and r <= 100000:
            total += r - l + 1
        else:
            return
    print(total)

if __name__ == "__main__":
    theater()