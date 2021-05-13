import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        sum_ = 0
        for j in range(m):
            sum_ += a[i][j] * b[j]
        sum_ += c
        if sum_ > 0:
            ans += 1
    print(ans)
            
if __name__ == '__main__':
    main()