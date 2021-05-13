def main():
    n = int(input())
    A = input().split()
    ans = list(reversed(A[1::2])) + A[::2]
    if n % 2 == 0:
        print(' '.join(ans))
    else:
        print(' '.join(list(reversed(ans))))


if __name__ == '__main__':
    main()
