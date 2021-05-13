# tenka1-2018-beginnerB - Exchange
def main():
    A, B, K = tuple(map(int, input().split()))
    for i in range(K):
        if i & 1 == 0:
            if A & 1:
                A -= 1
            A //= 2
            B += A
        else:
            if B & 1:
                B -= 1
            B //= 2
            A += B
    print(A, B)


if __name__ == "__main__":
    main()