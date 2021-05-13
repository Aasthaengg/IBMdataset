if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    flag = "Init"
    for i in range(1, n):
        if flag == "Init":
            if a[i - 1] == a[i]:
                pass
            elif a[i - 1] > a[i]:
                flag = "-"
            else:
                flag = "+"
        elif flag == "-":
            if a[i - 1] < a[i]:
                ans += 1
                flag = "Init"
        else:
            if a[i - 1] > a[i]:
                ans += 1
                flag = "Init"
    print(ans)
