def main():
    A, B, C = map(int, input().split())
    max_num = max(A, B, C)
    t = 3 * max_num - A - B - C
    ans = 0

    if t % 2 == 0:
        ans = int(t / 2)
    else:
        ans = int((t + 3) / 2)

    print(ans)


if __name__ == "__main__":
    main()
