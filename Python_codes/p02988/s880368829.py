n = int(input())
p = list(map(int, input().split()))
c = 0
for i in range(1, n - 1):
    t = p[i - 1:i + 2]
    t.sort()
    if t[1] == p[i]:
        c += 1
print(c)