n = int(input())

d = {}
for i in range(n):
    a = int(input())
    if a not in d:
        d[a] = 1
    else:
        if d[a]:
            d[a] = 0
        else:
            d[a] = 1

ans = 0
for v in d.values():
    ans += v
    
print(ans)