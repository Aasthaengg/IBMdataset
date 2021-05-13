n = int(input())
k = int(input())
x = list(map(int, input().split()))
ans = 0

for i in range(n):
    if x[i] >= k:
        ans += (x[i]-k)*2
    elif x[i] < k and k - x[i] < x[i]:
        ans += (k - x[i]) * 2
    else:
        ans += x[i]*2

print(ans)