def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, N+1):
        if (K-1)*x + 1 >= N:
            ans = x
            break
    print(ans)
main()