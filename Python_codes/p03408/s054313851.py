s = []
t = []
ans = 0

n = int(input())
for i in range(n):
    si = input()
    s.append(si)

m = int(input())
for i in range(m):
    ti = input()
    t.append(ti)

for c in s:
    cnt = s.count(c) - t.count(c)
    ans = max(ans, cnt)

print(ans)
