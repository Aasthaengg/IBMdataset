def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * n
    ans = []
    for i, a in enumerate(A[::-1]):
        i = n - i
        b = sum(B[i - 1::i])
        if b % 2 != a:
            ans.append(str(i))
            B[i - 1] = 1
    print(len(ans))
    print(' '.join(ans))

if __name__ == '__main__':
    main()
