l = list(map(int, input().split()))
ans = 0
while l[0] != l[1] or l[0] != l[2]:
    ans += 1
    l.sort()
    if l[2] > l[1]:
        l[0] += 1
        l[1] += 1
    else:
        l[0] += 2
print(ans)
