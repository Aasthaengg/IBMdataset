n = int(input())
A = [int(input()) for _ in range(n)]

p = {}
for a in A:
    if a in p:
        if p[a] == 1:
            p[a] = 0
            continue
    p[a] = 1
ans = 0
for i in p.values():ans += i
print(ans)