n = int(input())
p = list(map(int, input().split()))
ans = 0
 
for i in range(1, n-1):
    nums = [p[i-1], p[i], p[i+1]]
    if sorted(nums)[1] == p[i]:
        ans += 1
 
print(ans)