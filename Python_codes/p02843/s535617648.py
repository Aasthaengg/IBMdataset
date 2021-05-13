def main():
    X = int(input())
    N = X // 100
    M = X % 100
    if M == 0:
        print(1)
        return
    if M % 5 == 0 and M // 5 <= N:
        print(1)
    elif M % 5 > 0 and M // 5 + 1 <= N:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()