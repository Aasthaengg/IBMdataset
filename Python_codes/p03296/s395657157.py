if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    tmp = -1
    for i in range(n):
        if tmp == a[i]:
            ans += 1
            tmp = -1
        else:
            tmp = a[i]

    print(ans)
