n = int(input())
p = list(map(int, input().split()))
p.append(0)
for i in range(n): p[i] -= 1

ans = 0
for i in range(n):
    if p[i] == i:
        ans += 1
        p[i], p[i+1] = p[i+1], p[i]

print(ans)