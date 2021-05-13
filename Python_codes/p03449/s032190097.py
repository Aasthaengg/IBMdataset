import sys

input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A2 = list(map(int, input().split()))
    t = A[0]
    t2 = sum(A2)
    ans = t + t2
    for i in range(1, N):
        t += A[i]
        t2 -= A2[i-1]
        ans = max(ans, t+t2)
    print(ans)

if __name__ == '__main__':
    main()