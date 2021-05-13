def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = 1
    plus = 0
    minus = 0
    for i in range(n-1):
        if a[i + 1] - a[i] > 0:
            plus += 1
        elif a[i + 1] - a[i] < 0:
            minus += 1
        if plus and minus:
            res += 1
            plus = 0
            minus = 0
    print(res)
if __name__ == '__main__':
    main()