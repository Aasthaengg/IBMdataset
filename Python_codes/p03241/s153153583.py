def main():
    N, M = map(int, input().split())
    search = M//N + 1
    for s in range(search, 0, -1):
        sum_array = s * N
        if sum_array > M:
            continue
        remain = M - sum_array
        if remain % s == 0:
            print(s)
            return

if __name__ == "__main__":
    main()
