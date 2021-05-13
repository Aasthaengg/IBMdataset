n = int(input())
a = list(map(int, input().split()))
ans, pre = 0, 0
for i in a:
    if pre == i:
        ans += 1
        pre = 0
    else:
        pre = i
print(ans)
