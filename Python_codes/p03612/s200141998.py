n = int(input())
P = tuple(map(lambda x: int(x)-1, input().split()))
ans = 0
pre = P[0]
for i in range(n-1):
    if pre == i:
        ans += 1
    else:
        pre = P[i+1]
if pre == n-1:
    ans += 1
print(ans)
