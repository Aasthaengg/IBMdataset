def main():
    n, k = map(int, input().split())
    r = [0 for _ in range(k)]
    for i in range(1, n + 1):
        r[i % k] += 1
    answer = 0
    for i in range(k):
        if 2 * (k - i) % k == 0:
            answer += r[i] * (r[k - i if i > 0 else 0] ** 2)
    print(answer)


if __name__ == '__main__':
    main()

