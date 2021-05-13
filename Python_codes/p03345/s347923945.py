def main():
    a, b, c, k = map(int, input().split())

    if k % 2 == 0:
        ans = a - b
        if abs(ans) > 10 ** 18:
            print("Unfair")
        else:
            print(ans)
    else:
        ans = b - a
        if abs(ans) > 10 ** 18:
            print("Unfair")
        else:
            print(ans)


if __name__ == "__main__":
    main()
