n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=False)
count = 0
for i in range(n):
    if x>=a[i]:
        count += 1
        x -= a[i]
    else:
        break
if (x!=0)and(count==n):
    count -= 1
print(count)