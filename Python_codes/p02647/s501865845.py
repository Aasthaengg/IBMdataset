def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(k):
        imos = [0]*(n+1)
        finish = True
        for i, brightness in enumerate(a):
            if finish and brightness != n:
                finish = False
            begin = max(i - brightness, 0)
            end = i + brightness
            imos[begin] += 1
            if end < n:
                imos[end + 1] -= 1
        if finish:
            break
        for i in range(n-1):
            imos[i+1] += imos[i]
        a = imos[:-1]
    print(*a, sep=" ")


if __name__ == "__main__":
    main()
