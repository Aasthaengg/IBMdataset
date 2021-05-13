def main():
    n = int(input())

    for i in range(1, 50000):
        if i * 108 // 100 == n:
            print(i)
            break
    else:
        print(":(")


if __name__ == "__main__":
    main()
