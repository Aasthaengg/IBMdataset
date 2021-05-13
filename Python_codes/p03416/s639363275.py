a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    si = str(i)
    l = len(si)
    check = True
    for j in range(l // 2):
        if si[j] != si[(-j - 1)]:
            check = False
            break
    if check:
        ans += 1
print(ans)
