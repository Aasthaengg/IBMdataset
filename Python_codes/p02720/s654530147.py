K = int(input())

lst = [i for i in range(1, 10)]

if K < 10:
    print(K)
else:
    now = 0
    K -= 9
    ans = 0
    while True:
        md = lst[now] % 10
        for i in range(10):
            if abs(md - i) <= 1:
                K -= 1
                ans = lst[now] * 10 + i
                lst.append(ans)
                if K == 0:
                    print(ans)
                    exit()
        now += 1