def main():
    N, K = list(map(int, input().split(' ')))
    x = list(map(int, input().split(' ')))  # already sorted
    left = - min([x[0], 0])
    right = max([x[K - 1], 0])
    min_t = min([2 * left + right, left + 2 * right])
    for i in range(N):
        if i + K - 1 > N - 1:
            break
        left = - min([x[i], 0])
        right = max([x[i + K - 1], 0])
        min_t = min([min_t, min([2 * left + right, left + 2 * right])])
    print(min_t)


if __name__ == '__main__':
    main()