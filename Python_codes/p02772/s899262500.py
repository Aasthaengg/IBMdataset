def main():
    n = int(input())
    a = list(map(int, input().split()))

    for num in a:
        if num % 2 == 0:
            if num % 3 != 0 and num % 5 != 0:
                break
    else:
        print("APPROVED")
        return
    print("DENIED")


if __name__ == "__main__":
    main()

