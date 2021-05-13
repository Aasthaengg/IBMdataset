def main():
    lst = [int(input()) for _ in range(5)]
    k = int(input())

    if lst[4] - lst[0] > k:
        print(":(")
    else:
        print("Yay!")


if __name__ == "__main__":
    main()
