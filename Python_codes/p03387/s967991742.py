l = map(int, input().split())
l = list(l)
l.sort()

ans = 0
while l[2] > l[1]:
    ans += 1
    l[1] += 1
    l[0] += 1

while l[1] > l[0]:
    ans += 1
    l[0] += 2

if l[0] > l[1]:
    ans += 1

print(ans)
