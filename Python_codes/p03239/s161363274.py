def mi():
    return map(int, input().split())

def main():
    N, T = mi()
    ct = [map(int, input().split()) for _ in range(N)]
    c, t = [list(i) for i in zip(*ct)]
    m = 10**100
    bl = False
    for i in range(N):
        if t[i] <= T:
            m = min(m, c[i])
            bl = True
    print(m if bl else 'TLE')


if __name__ == '__main__':
    main()