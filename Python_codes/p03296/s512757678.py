n = int(input())
a = list(map(int, input().split()))
ans = 0
flag = False
for i in range(1, n):
    if a[i] == a[i - 1]:
        if not flag:
            ans += 1
        flag = not flag
    else:
        flag = False
print(ans)