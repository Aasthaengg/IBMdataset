def main():
    n = int(input())
    f = [list(map(int, input().split())) for _ in range(n)]
    p = [list(map(int, input().split())) for _ in range(n)]
    answer = -float("inf")
    for i in range(1, pow(2, 10)):
        now = 0
        cnt = [0 for _ in range(n)]
        for j in range(10):
            if (i >> j) & 1:
                for k in range(n):
                    if f[k][j]:
                        cnt[k] += 1
        for j in range(n):
            now += p[j][cnt[j]]
        answer = max(answer, now)
    print(answer)


if __name__ == '__main__':
    main()

