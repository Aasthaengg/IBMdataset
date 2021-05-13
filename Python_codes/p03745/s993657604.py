n = int(input())
a_li = list(map(int,input().split()))
if n < 3:
    print(1)
    exit()
ans = 1
flag = "flat"
for i in range(1,n):
    if a_li[i-1] > a_li[i]:
        if flag == "up":
            ans += 1
            flag = "flat"
            continue
        flag = "down"
    elif a_li[i-1] < a_li[i]:
        if flag == "down":
            ans += 1
            flag = "flat"
            continue
        flag = "up"
    else:
        if flag == "flat":
            flag = "flat"
print(ans)