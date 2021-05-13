def main():
    import sys
    input = sys.stdin.buffer.readline
    N, H, W = (int(i) for i in input().split())
    AB = [[int(i) for i in input().split()] for j in range(N)]
    ans = 0
    for a, b in AB:
        ans += min(a//H, b//W)
    print(ans)


if __name__ == '__main__':
    main()
