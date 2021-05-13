def main():
    A, B, K = (int(i) for i in input().split())
    for k in range(K):
        if k & 1:
            if B & 1:
                B -= 1
            A += B//2
            B //= 2
        else:
            if A & 1:
                A -= 1
            B += A//2
            A //= 2
    print(A, B)


if __name__ == '__main__':
    main()
