n, t = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    ans += min(l[i+1]-l[i], t)
print(ans+t)