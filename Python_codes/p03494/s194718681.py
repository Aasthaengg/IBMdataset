# 2020-08-27, Thu

n = int(input())
lis = list(map(int, input().split()))
ans = 0

while (1):
    count = 0
    for i in range(n):
        if lis[i] % 2 == 0:
            lis[i] //= 2
            count += 1
    if count == n:
        ans += 1
    else:
        break

print(ans)