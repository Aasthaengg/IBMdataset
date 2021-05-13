def main():
    N = int(input())
    is_able = False

    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                is_able = True

    if is_able:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
