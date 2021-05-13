s, t  = map(int, input().split())
u = list(map(int,input().split()))
ans = t
for i in range(1,s):
    if u[i] - u[i -1] >= t:
        ans += t
    if u[i] - u[i - 1] < t:
        ans += u[i] - u[i - 1]
print(ans)