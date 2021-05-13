def main():
    N, M, K = (int(i) for i in input().split())
    ans = set()
    for i in range(M+1):
        for j in range(N+1):
            if N-j >= 0 and M-i >= 0:
                ans.add((N-j)*i + (M-i)*j)
    if K in ans:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
