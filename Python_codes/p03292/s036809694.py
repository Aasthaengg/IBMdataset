def main():
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    print(abs(A[1] - A[0]) + abs(A[2] - A[1]))

if __name__ == '__main__':
    main()