def main():
    import sys
    readline = sys.stdin.readline
    # readlines = sys.stdin.readlines
    N, T = map(int, input().split())
    A = list(map(int, readline().split()))

    L = float('inf')
    cnt = 0
    profit = 0
    for a in A:
        if a - L > profit:
            cnt = 1
            profit = a - L
        elif a - L == profit:
            cnt += 1
        
        if a < L:
            L = a
    
    print(cnt)


if __name__ == "__main__":
    main()
