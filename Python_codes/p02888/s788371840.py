from bisect import bisect_right
import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    *L, = map(int, input().split())
    L.sort()
    ans = 0
    for i in range(2, N):
        for j in range(i):
            k = bisect_right(L, L[i] - L[j], j + 1, i)
            ans += i - k
    print(ans)

if __name__ == '__main__':
    main()
