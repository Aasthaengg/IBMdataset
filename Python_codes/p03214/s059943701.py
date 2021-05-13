n = int(input())
l = list(map(int,input().split()))
me = sum(l)/n
ans = -1
now = 10**10
for i in range(n):
    if abs(me-l[i])<now:
        now = abs(me-l[i])
        ans = i
print(ans)