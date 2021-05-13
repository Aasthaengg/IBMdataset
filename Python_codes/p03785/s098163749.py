n,c,k = map(int,input().split())
t = [0]*n
for i in range(n):
    t[i] = int(input())
t = sorted(t)
ans = 0
s = 0
u = float("Inf")
for i in range(n-1):
    s += 1
    u = min(u, t[i])
    if s == c or t[i+1] > u + k:
        ans += 1
        s = 0
        u = float("Inf")
print(ans+1)