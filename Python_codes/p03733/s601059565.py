n, t = map(int, input().split())
tl = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    if tl[i+1] - tl[i] >= t:
        ans += t
    else:
        ans += tl[i+1] - tl[i]

print(ans+t)