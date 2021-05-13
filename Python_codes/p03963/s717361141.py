def main():
    n, k = [int(e) for e in input().split()]
    ans = k * ((k - 1)**(n - 1))

    print(ans)


if __name__ == "__main__":
    main()
