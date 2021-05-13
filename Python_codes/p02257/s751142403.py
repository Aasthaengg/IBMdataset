n = int(input())
ans = 0
for i in range(n):
    k = int(input())
    j = 2
    flag = 0
    while k/j >= j:
        if k % j == 0:
            flag = 1
            break
        j += 1
    if flag == 0:
        ans += 1
print(ans)