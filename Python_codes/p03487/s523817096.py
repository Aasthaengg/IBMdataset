n = int(input())
a = list(map(int, input().split()))
ans = 0
a.sort()
r = [[a[0], 1]]
c = 1
for i in range(n-1):
    if a[i] == a[i+1]:
        r[-1][1] += 1
    else:
        r.append([a[i+1], 1])
for i in range(len(r)):
    if r[i][0] <= r[i][1]:
        ans += r[i][1] - r[i][0]
    else:
        ans += r[i][1]
print(ans)