def main():
    M = 10 ** 5
    N, K = list(map(int, input().split(' ')))
    count = [0 for _ in range(M + 1)]
    for _ in range(N):
        a, b = list(map(int, input().split(' ')))
        count[a] += b
    ans = 0
    while K > 0:
        ans += 1
        K -= count[ans]
    print(ans)


if __name__ == '__main__':
    main()