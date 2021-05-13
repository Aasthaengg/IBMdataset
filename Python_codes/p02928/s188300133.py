n, k= map(int, input().split())
lis = list(map(int, input().split()))

mod = 10**9 + 7

ans = 0
right = 0
zenbu = 0

for i in range(n-1):
    for j in range(i,n):
        if lis[i] > lis[j]:
            right += 1
for i in range(n):
    for j in range(n):
        if lis[i] > lis[j]:
            zenbu += 1
    
t = (k-1)*k
ans += right*k
ans +=(t//2)*zenbu
ans %= mod

print(ans)