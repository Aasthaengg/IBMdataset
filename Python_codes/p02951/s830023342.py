def main():
    A, B, C = map(int, input().split())

    t = min(A - B, C)
    ans = C - t

    print(ans)


if __name__ == "__main__":
    main()
