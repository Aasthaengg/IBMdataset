def main():
    n, k = map(int, input().split())
    ans = k * ((k-1)**(n-1))
    print(ans)


if __name__ == "__main__":
    main()
