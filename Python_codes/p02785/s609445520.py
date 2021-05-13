n,k = map(int, input().split())
H = sorted(list(map(int, input().split())))[::-1]
ans = 0
for h in H:
    if k>0:
        k -= 1
        continue
    ans += h
print(ans)