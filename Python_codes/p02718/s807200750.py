n,m = input().split()
n = int(n)
m = int(m)
a = list(map(int, input().split()))
res = 0
for c in a:
    if c >= sum(a) / (4 * m):
        res += 1
if res >= m:
    print("Yes")
else:
    print("No")
