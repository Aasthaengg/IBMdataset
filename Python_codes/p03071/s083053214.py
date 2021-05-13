def main():
    A, B = map(int, input().split())
    coin = 0
    for i in range(2):
        if A > B:
            coin += A
            A -= 1
        else:
            coin += B
            B -= 1
    print(coin)
if __name__ == "__main__":
    main()