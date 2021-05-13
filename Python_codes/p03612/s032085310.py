n = int(input())
p = [int(x) - 1 for x in input().split()]

ans = 0
num = -1
for i in range(n - 1):
    if num == i:
        continue
    if p[i] == i:
        if p[i + 1] == i + 1:
            num = i + 1
        
        ans += 1

if num != n - 1 and p[n - 1] == n - 1:
    ans += 1
    
print(ans)