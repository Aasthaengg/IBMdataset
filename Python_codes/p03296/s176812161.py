n = int(input())
a = list(map(int,input().split()))

s = []
ap = a[0]
count = 0
for i in range(n):
    if ap == a[i]:
        count += 1
    else:
        if count > 1:
            s.append(count)
        ap = a[i]
        count = 1
if count > 1:
    s.append(count)

ans = 0
for x in s:
    ans += x//2
print(ans)