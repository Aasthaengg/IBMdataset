def main():
    N = int(input())
    
    if N % 10 == 0:
        N -= 1
    else:
        first = 0
        M = N
        while True:
            d = M % 10
            M //= 10
            if M == 0:
                first = d
                break

        if N != (first + 1) * (10 ** (len(str(N)) - 1)) - 1:
            N = (first) * (10 ** (len(str(N)) - 1)) - 1

    ans = 0
    N = str(N)
    for d in N:
        ans += int(d)

    print(ans)

if __name__ == "__main__":
    main()