import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    CNT, ans = 0, 0
    for i in range(N):
        CNT = sum(A[0:i+1]) + sum(B[i:N+1])
        ans = max(ans, CNT)
    print(ans)

if __name__ == '__main__':
    main()