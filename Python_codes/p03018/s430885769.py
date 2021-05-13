a = list(input())
ans = 0
i = 0

a_count = 0  # 連続ででたAの個数
# BC_count = 0  # BC出てきたらそれまでのAの数分

while i < len(a)-1:
    if a[i] == "A":
        count = "A"
        a_count += 1
    elif a[i]+a[i+1] == "BC":
        count = "BC"
        ans += a_count
        i += 1
    else:
        count = "VBNM"
        a_count = 0
    # print(a_count, ans, i, count)
    i += 1

print(ans)