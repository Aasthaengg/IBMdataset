n = int(input())
v = sorted(list(map(int, input().split())))
ans = v[0]
for x in v[1:n]:
    ans = (ans + x) / 2
print(ans)