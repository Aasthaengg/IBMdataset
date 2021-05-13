def main():
    A, B = map(int, input().split())
    if A == B:
        ans = A + B
    else:
        ans = max(A, B)
        ans = ans + (ans - 1)
    print(ans)


if __name__ == "__main__":
    main()
