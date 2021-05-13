def main():
    A, B, C = (int(x) for x in input().split())
    if A - B >= C:
        ans = 0
    else:
        ans = C - (A - B)
    print(ans)


if __name__ == "__main__":
    main()
