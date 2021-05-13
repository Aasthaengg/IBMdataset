n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
a = sorted([v[i]-c[i] for i in range(n)],reverse=True)
ans = 0
for j in a:
    if j <= 0:
        break
    ans += j
print(ans)