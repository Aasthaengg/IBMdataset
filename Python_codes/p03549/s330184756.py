def main():
    N, M = map(int, input().split())
    t = 1900*M + 100*(N-M)
    print(t*(2**M))


if __name__ == "__main__":
    main()
