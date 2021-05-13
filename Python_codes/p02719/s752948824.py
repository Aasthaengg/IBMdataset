def main():
    n, k = map(int, input().split())
    if n - k > k:
        n_k = (n-k) // k
        minv = n - k * n_k
    else:
        minv = n

    def min_x(x):
        minv = x
        for _ in range(2):
            if abs(minv - k) < abs(minv):
                minv = abs(minv - k)
            else:
                print(minv)
                exit()
        print(minv)

    min_x(minv)


if __name__ == '__main__':
    main()