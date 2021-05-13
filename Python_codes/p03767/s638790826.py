def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_s = sorted(a, reverse=True)
    res = 0
    num = 0
    for i in range(n*3):
        if i % 2 == 1 and num < n:
            res = res + a_s[i]
            num += 1
    print(res)
if __name__ == '__main__':
    main()