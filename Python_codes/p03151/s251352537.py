n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
cnt = 0
lack = 0

for i in range(n):
    if a[i] < b[i]:
        cnt += 1
        lack += b[i] - a[i]
    elif a[i] > b[i]:
        c.append(a[i] - b[i])

c = sorted(c)[::-1]
asum = sum(a)
bsum = sum(b)

if asum < bsum:
    print(-1)
    exit()
if cnt == 0:
    print(0)
    exit()

for i in c:
    lack -= i
    cnt += 1
    if lack <= 0:
        break

print(cnt)