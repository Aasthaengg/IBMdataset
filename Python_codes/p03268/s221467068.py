def main():
    N, K = (int(i) for i in input().split())
    c0 = 0
    c1 = 0
    for num in range(1, N+1):
        if num % K == 0:
            c0 += 1
        elif K % 2 == 0 and num % K == K//2:
            c1 += 1
    print(c0*c0*c0 + c1*c1*c1)


if __name__ == '__main__':
    main()
