n = int(input())
lst = list(map(int,input().split()))
ans = 0
for i in range(n):
  for j in range(i + 1, n):
    ans = ans + lst[i]*lst[j]
print(ans)