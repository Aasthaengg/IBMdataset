def main():
    N = int(input())
    d = [int(input()) for _ in range(N)]

    d_s = list(set(d))
    print(len(d_s))


if __name__ == "__main__":
    main()
