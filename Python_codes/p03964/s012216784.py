def main():
    N = int(input())
    TA = [[int(_) for _ in input().split()] for __ in range(N)]
    x, y = TA[0] #初期値
    for i in range(1, N):
        T, A = TA[i]
        if x%T != 0:
            x += T - x%T
        if A * x // T < y:
            if y%A != 0:
                y += A - y%A
            x = T * y // A
        else:
            y = A * x // T
    print(x+y)
    return

if __name__ == '__main__':
    main()
