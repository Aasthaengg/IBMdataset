n = int(input())
a = sorted(list(map(int, input().split())))
a.reverse()
ans = []
c = 1
for i in range(1, n):
    if len(ans) >= 2:
        break
    if a[i] == a[i - 1]:
        c += 1
        m = a[i]
    else:
        if c >= 2:
            ans.append([a[i - 1], c])
        c = 1
if len(ans) < 2 and c >= 2:
    ans.append([a[n - 1], c])

if len(ans) >= 2:
    if ans[0][1] >= 4:
        print(ans[0][0] ** 2)
    else:
        print(ans[0][0] * ans[1][0])
elif len(ans) == 1:
    if ans[0][1] >= 4:
        print(ans[0][0] ** 2)
    else:
        print(0)
else:
    print(0)