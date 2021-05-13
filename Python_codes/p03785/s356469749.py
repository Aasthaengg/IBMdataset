n,c,k = map(int,input().split())
t = []
for _ in range(n):
    a = int(input())
    t.append(a)
t.sort()

ans = 0
cnt = 1
rng = t[0]+k

for i in range(1,n):
    if t[i] <= rng and cnt < c:
        cnt += 1
    else:
        rng = t[i]+k
        cnt = 1
        ans += 1
ans += 1

print(ans)