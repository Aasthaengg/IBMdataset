N = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(N-1):
    if a[i] > a[i+1] >= 0:
        a[i+1] += a[i]
        ans.append((i+1, i+2))
    if a[i] >= 0 > a[i+1] and a[i] + a[i+1] >= 0:
        a[i+1] += a[i] * 2
        ans.append((i+1, i+2))
        ans.append((i+1, i+2))
for i in range(N-1)[::-1]:
    if 0 >= a[i] > a[i+1]:
        a[i] += a[i+1]
        ans.append((i+2, i+1))
    if a[i] >= 0 > a[i+1]:
        a[i] += a[i+1] * 2
        ans.append((i+2, i+1))
        ans.append((i+2, i+1))
print(len(ans))
for x, y in ans:
    print(x, y)
