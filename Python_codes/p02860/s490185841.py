def main():
    N = int(input())
    S = input().rstrip()
    if N % 2 == 1:
        print("No")
    elif S[:int(N/2)] == S[int(N/2):]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
