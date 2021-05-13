def main():
    # import sys
    # readline = sys.stdin.buffer.readline
    # readlines = sys.stdin.buffer.readlines
    N, M = map(int, input().split())
    cnt = 0

    if N >= M // 2:
        cnt = M // 2
    else:
        cnt += N
        M -= 2 * N
        cnt += M // 4
    
    print(cnt)


if __name__ == "__main__":
    main()
