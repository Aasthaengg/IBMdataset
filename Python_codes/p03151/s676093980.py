n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
cnt = 0
lack = 0

for i in range(n):
    diff = a[i] - b[i]
    if diff < 0:
        cnt += 1
        lack -= diff
    elif diff > 0:
        c.append(diff)

c = sorted(c)[::-1]

if sum(a) < sum(b):
    print(-1)
    exit()

for i in c:
    if lack <= 0:
        break
    lack -= i
    cnt += 1

print(cnt)