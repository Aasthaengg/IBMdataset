a = []
b = []
ans = 'No'

for i in range(3):
    a.extend([int(s) for s in input().split()])
n = int(input())
for j in range(n):
    value = int(input())
    b.append(value)
    if value in a:
        a[a.index(value)] = '*'

if a[0] == a[1] == a[2] or a[3] == a[4] == a[5] or a[6] == a[7] == a[8] or a[0] == a[4] == a[8]:
    ans = 'Yes'
if a[0] == a[3] == a[6] or a[1] == a[4] == a[7] or a[2] == a[5] == a[8] or a[2] == a[4] == a[6]:
    ans = 'Yes'
print(ans)