def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))[::-1]
    if N % 2 == 1:
        print(sum(A[:N//2]) + sum(A[1:N//2+1]))
    else:
        print(sum(A[:N//2-1]) + sum(A[1:N//2]) + A[N//2-1])


if __name__ == '__main__':
    main()
