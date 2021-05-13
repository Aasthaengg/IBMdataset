N = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(N):
    num = a[i]
    tmp = 0
    while (num % 2 == 0 and num > 0):
        num /= 2
        tmp += 1
    ans += tmp

print(ans)