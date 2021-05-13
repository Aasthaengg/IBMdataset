def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    cur = 0
    ans = 0
    for i in range(N):
        cur += A[i]
        ans += 1
        if i == N-1:
            break
        if A[i+1] <= cur*2:
            continue
        else:
            ans = 0
    print(ans)


if __name__ == '__main__':
    main()
