def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    top = a[0]
    ans = 0

    for i in range(n):
        if a[i] < top:
            ans += top - a[i]
        else:
            top = a[i]

    print(ans)


main()
