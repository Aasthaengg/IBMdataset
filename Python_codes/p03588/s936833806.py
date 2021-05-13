def main():
    N = int(input())
    A = [[int(i) for i in input().split()] for j in range(N)]
    A.sort(key=lambda p: p[1])
    print(sum(A[0]))


if __name__ == '__main__':
    main()
