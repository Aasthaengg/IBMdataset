n = int(input())
k = int(input())
ans = 1
for _ in range(n):
    ans = ans * 2 if ans * 2 < ans + k else ans + k
print(ans)