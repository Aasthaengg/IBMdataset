n, k = map(int, input().split())
if (n - 2) * (n-1) // 2 < k:
    print(-1)
else:
    #全部の頂点をつなぐ
    ans = []
    for i in range(2,n+1):
        ans.append([1, i])
    num = (n-2) * (n-1) // 2
    for i in range(2,n+1):
        for j in range(i+1,n+1):
            if num == k:
                print(len(ans))
                for ans_array in ans:
                    print("{} {}".format(*ans_array))
                exit()
            num -= 1
            ans.append([i,j])
    print(len(ans))
    for ans_array in ans:
        print("{} {}".format(*ans_array))
