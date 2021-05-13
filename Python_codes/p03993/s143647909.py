def main():
    N = int(input())
    A = [int(i)-1 for i in input().split()]

    ans = 0
    for i, a in enumerate(A):
        if A[a] == i:
            ans += 1
    print(ans//2)


if __name__ == '__main__':
    main()
