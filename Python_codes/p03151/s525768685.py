def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    if sum(a) < sum(b):
        print(-1)
        return

    sub = []
    t = 0
    cnt = 0
    for i in range(n):
        if a[i] < b[i]:
            cnt += 1
            t += b[i] - a[i]
        else:
            sub.append(a[i]-b[i])

    if cnt == 0:
        print(0)
        return

    ans = cnt
    i = 0
    sub.sort(reverse=True)
    while t > 0:
        ans += 1
        t -= sub[i]
        i += 1
    print(ans)








if __name__ == '__main__':
    main()
