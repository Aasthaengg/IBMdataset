def main():
    N = int(input())
    A = dict()

    for _ in range(N):
        num = int(input())
        if num in A:
            del A[num]
        else:
            A[num] = 1

    print(len(A))


if __name__ == "__main__":
    main()
