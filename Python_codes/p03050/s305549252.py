def main():
    N = int(input())

    i = 1
    out = 0
    while i*i <= N:
        if N%i == 0 and i < N//i-1:
            out += (N//i - 1)
        i += 1
    print(out)
    return

if __name__ == '__main__':
    main()
