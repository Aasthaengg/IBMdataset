def main():
    K = [int(input()) for i in range(5)]
    k = int(input())
    ans = True
    for i in range(5):
        for j in range(i + 1, 5):
            if K[j] - K[i] > k:
                ans = False
                break

    if ans:
        print("Yay!")
    else:
        print(":(")


if __name__ == "__main__":
    main()
