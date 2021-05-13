n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
p.sort()

ans = 0
for i in range(len(p)):
    if i == len(p)-1:
        ans += p[i]//2
    else:
        ans += p[i]

print (ans)
