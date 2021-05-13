def main():
    A = int(input())
    B = int(input())

    num = [1, 2, 3]

    num.remove(A)
    num.remove(B)

    print(*num)


if __name__ == "__main__":
    main()
