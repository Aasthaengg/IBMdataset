N = int(input())


def GetDivider(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt


ans = 0
for i in range(1, N+1):
    if GetDivider(i) == 8:
        if i % 2 != 0:
            ans += 1
print(ans)
