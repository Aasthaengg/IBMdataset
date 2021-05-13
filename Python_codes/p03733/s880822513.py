def main():
    N, T = (int(i) for i in input().split())
    A = [int(i) for i in input().split()]
    ans = 0
    for i in range(N-1):
        ans += min(A[i+1] - A[i], T)
    ans += T
    print(ans)


if __name__ == '__main__':
    main()
