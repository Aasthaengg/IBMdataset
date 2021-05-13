def main():
    X = int(input())
    A = int(input())
    B = int(input())
    ans = X
    if A <= ans:
        ans -= A
    while ans - B >= 0:
        ans -= B
    print(ans)


if __name__ == '__main__':
    main()
