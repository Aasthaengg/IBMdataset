n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = a[-1]
j = -2
flag = 0
for i in range(n-2):
    ans += a[j]
    if flag:
        j -= 1
        flag = 0
    else:
        flag = 1

print(ans)