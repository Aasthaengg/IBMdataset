n = int(input())
ans = [0, 0]
for i in range(n):
    [t, h] = input().split()
    sort = [t, h]
    sort.sort()
    if t==h:
        ans[0] += 1
        ans[1] += 1
    elif [t, h]==sort:
        ans[1] += 3
    else:
        ans[0] += 3

print(ans[0], ans[1])