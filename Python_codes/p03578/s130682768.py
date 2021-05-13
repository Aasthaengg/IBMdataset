
n = int(input())
d = sorted(map(int, input().split()))
m = int(input())
t = sorted(map(int, input().split()))
if n < m:
    print("NO")
    exit()

p = 0
ans = True

for i in range(m):
    while p < n and d[p] < t[i]:
        p += 1
    if p >= n or d[p] > t[i]:
        ans = False
    p += 1
print(["NO", "YES"][ans])
