def main():
    N = int(input())
    if N % 2 == 0:
        print((N // 2) * (N-1))
    else:
        print(N * ((N-1)//2))

if __name__ == '__main__':
    main()
