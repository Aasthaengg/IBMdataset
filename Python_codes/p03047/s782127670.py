n,k = map(int,input().split())
n1 = n + 1
ans = 0
for i in range(1,n1):
    if n >= k:
        ans += 1
        n -= 1
    else:
        break
print(ans)