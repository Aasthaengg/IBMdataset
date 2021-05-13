def main():
    N, K = (int(i) for i in input().split())
    cnt = 0
    for i in range(1, 2*10**5+1):
        if K*i <= N:
            cnt += 1
        else:
            break
    addcnt = 0
    if K % 2 == 0:
        for i in range(1, 2*10**5+1, 2):
            if (K//2)*i <= N:
                addcnt += 1
            else:
                break
    ans = cnt**3 + addcnt**3
    print(ans)


if __name__ == '__main__':
    main()
