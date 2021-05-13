def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N):
        A[i] -= i+1
    A.sort()
    b = A[N//2]
    print(sum([abs(a - b) for a in A]))


if __name__ == '__main__':
    main()
