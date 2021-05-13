def main():
    N = int(input())
    A = input()
    B = input()
    C = input()
    ans = 0
    for i in range(N):
        s = set()
        s.add(A[i])
        s.add(B[i])
        s.add(C[i])
        if len(s) == 2:
            ans += 1
        elif len(s) == 3:
            ans += 2
    print(ans)


if __name__ == '__main__':
    main()
