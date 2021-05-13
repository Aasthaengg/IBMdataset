import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(K):
        b = [0] * (N+1)
        for j in range(N):
            a = A[j]
            b[max(j-a, 0)] += 1
            b[min(j+a+1, N)] -= 1
        for k in range(1,N+1):
            b[k] += b[k-1]
        b = b[:N]
        if b == A:
            break
        else:
            A = b
    print(*A)

if __name__ == '__main__':
    main()