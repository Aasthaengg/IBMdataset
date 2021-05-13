def main():
    N, M = map(int, input().split())
    maxM = M//N + 1
    for m in range(maxM, 0, -1):
        tmp = m * N
        remain = M - tmp
        check = remain % m
        if check == 0 and remain >= 0:
            print(m)
            return

if __name__ == "__main__":
    main()
