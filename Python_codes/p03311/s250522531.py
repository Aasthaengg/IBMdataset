def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [a[i] - i - 1 for i in range(n)]
    c.sort()

    b = c[n // 2]
    sad = sum([abs(cc - b) for cc in c])
    print(sad)


main()
