n = int(input())
k = int(input())
ans = 1
for _ in range(n):
    ans += ans if ans < k else k
print(ans)