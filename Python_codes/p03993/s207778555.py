def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if A[A[i] - 1] - 1 == i:
            ans += 1
    print(ans // 2)

if __name__ == '__main__':
    main()
