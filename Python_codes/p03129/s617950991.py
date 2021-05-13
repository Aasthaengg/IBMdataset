def slove():
    import sys
    input = sys.stdin.readline
    n, k = list(map(int, input().rstrip('\n').split()))
    print("YES" if (n + 2 - 1) // 2 >= k else "NO")


if __name__ == '__main__':
    slove()
