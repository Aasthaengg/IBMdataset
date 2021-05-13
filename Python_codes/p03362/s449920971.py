from math import floor

n = int(input())

ans_list = []
ans_num = 0
ans = 1
while ans_num < n:
    ans += 5
    for i in range(2, floor(ans ** 0.5) + 1):
        if ans % i == 0:
            break
    else:
        ans_list.append(ans)
        ans_num += 1
print(*ans_list)