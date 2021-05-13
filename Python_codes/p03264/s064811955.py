def main():
    k = int(input())
    if k % 2 == 0:
        even = k // 2
        odd = even
    else:
        even = k // 2
        odd = k - even

    print(even * odd)


if __name__ == "__main__":
    main()
