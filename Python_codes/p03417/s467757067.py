def main():
    N, M = map(int, input().split())
    if N == 1:
        if M > 2:
            print(M-2)
        elif M == 2:
            print(0)
        else:
            print(1)
    elif M == 1:
        if N > 2:
            print(N-2)
        elif N == 2:
            print(0)
        else:
            print(1)
    elif N == 2 or M == 2:
        print(0)
    else:
        print((N-2)*(M-2))
if __name__ == "__main__":
    main()