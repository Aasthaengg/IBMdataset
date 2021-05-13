def main():
    r, D, x = map(int, input().split())
    for i in range(1, 11):
        k = r * x - D
        x = k
        print(k)


if __name__ == "__main__":
    main()
