n = int(input())
h = list(map(int, input().split()))
ans = 0
flag = 0
for i in range(102):
    flag = 0
    for j in range(n):
        if flag == 0 and h[j] != 0:
            ans += 1
            flag = 1
            h[j] -= 1
        elif flag == 1 and h[j] != 0:
            h[j] -= 1
        elif flag == 1 and h[j] == 0:
            flag = 0
    if sum(h) <= 0:
        print(ans)
        break