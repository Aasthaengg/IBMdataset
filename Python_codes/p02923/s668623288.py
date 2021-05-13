n = int(input())
H = tuple(map(int, input().split()))
ans = 0
i = 0
ph = 0
for h in H:
    if ph >= h:
        i += 1
    else:
        ans = max(ans, i)
        i = 0
    ph = h
else:
    ans = max(ans, i)
print(ans)
