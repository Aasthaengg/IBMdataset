def main():
    A, B, C, K = map(int, input().split())

    d = abs(A - B)
    if d > 10**18:
        print("Unfair")

    else:
        if A > B:
            if K % 2 == 0:
                print(d)
            else:
                print(-d)

        elif A < B:
            if K % 2 == 0:
                print(-d)
            else:
                print(d)

        else:
            print("0")

if __name__ == "__main__":
    main()