n, m = map(int, input().split())
a = [int(s) for s in input().split()]
limit = sum(a) / (m * 4)
a.sort(reverse=True)
for i in a[: m]:
    if i < limit:
        ans = 'No'
        break
    else:
        ans = 'Yes'
print(ans)