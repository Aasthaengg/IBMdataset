def main():
    n = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for idx in range(1, n-1):
        if P[idx] == sorted([P[idx-1], P[idx], P[idx+1]])[1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
