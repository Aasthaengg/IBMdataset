# C - Lower
def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    ans = []

    if n == 1:
        print(0)
        exit()
    for i in range(n-1):
        if h[i] >= h[i+1]:
            cnt += 1
            if i == n-2:
                ans.append(cnt)

        else:
            ans.append(cnt)
            cnt = 0
    print(max(ans))


if __name__ ==  "__main__":
    main()