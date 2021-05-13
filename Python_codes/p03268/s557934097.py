def main():
    N, K = map(int, input().split())

    if K&1: # Kが奇数
        tmp = N//K
        print(tmp**3)
    else:   # Kが偶数
        tmp = N//K
        tmp2 = tmp
        if N%K >= K//2:
            tmp2 += 1
        print(tmp**3 + tmp2**3)

if __name__ == "__main__":
    main()