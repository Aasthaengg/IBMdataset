def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    s = sum(a)
    minx = s
    sum_a = 0

    for i in range(n):
        sum_a += a[i]
        minx = min(minx, abs(sum_a - (s - sum_a)))

    print(minx)


if __name__ == "__main__":
    main()