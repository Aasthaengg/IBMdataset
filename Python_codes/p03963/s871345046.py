n,k = map(int,input().split())
ans = 1
for i in range(n):
    if i == 0:
        ans *= k
        continue
    ans *= (k - 1)
print(ans)