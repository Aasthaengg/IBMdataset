def main():
    N, A, B = map(int, input().split())
    if A > B:
        return 0
    if N == 1:
        if A != B:
            return 0
        else:
            return 1
    if N == 2:
        return 1

    mn = A * (N - 1) + B
    mx = A + B * (N - 1)
    return mx - mn + 1


if __name__ == "__main__":
    print(main())