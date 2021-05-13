n = int(input())
a = list(map(int,input().split()))
ans = [-1] * n
total = 0

for i in a:
    total ^= i
    
for i in range(n):
    ans[i] = total ^ a[i]
    
print(*ans)