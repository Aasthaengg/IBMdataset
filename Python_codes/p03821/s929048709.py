n = int(input())
p = []
for i in range(n):
    a , b = map(int,input().split())
    p.append([a,b])
ans = 0
for i in reversed(range(n)):
    if (p[i][0] + ans) % p[i][1] != 0:
        ans += p[i][1] - ((p[i][0] + ans)%p[i][1])
print(ans)