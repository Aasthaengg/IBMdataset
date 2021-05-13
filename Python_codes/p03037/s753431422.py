n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
haba = a[0]
for i in a:
    if haba[0] <= i[0] <= haba[1]:
        haba[0] = i[0]
    elif haba[1] < i[0]:
        print(0)
        exit()
    if haba[0] <= i[1] <= haba[1]:
        haba[1] = i[1]
    elif i[1] < haba[0]:
        print(0)
        exit()
if n < haba[0]:
    ans = 0
elif haba[0] <= n <= haba[1]:
    ans = n - haba[0] + 1
else:
    ans = haba[1] - haba[0] + 1
print(ans)