import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    h = [int(input()) for i in range(N)]
    H = sorted(h)

    ans = 10**9 +1
    for i in range(N-K+1):
        high = H[i+K-1] - H[i] 
        ans = min(ans, high)
    print(ans)

if __name__ == '__main__':
    main()