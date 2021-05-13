n, x = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
# box = []
cnt = 0

for i in range(n):
    x = x - a[i]
    if(x >= 0):
        cnt += 1
    else:
        break
if(x != 0 and cnt == n):
    cnt -= 1
print(cnt)
