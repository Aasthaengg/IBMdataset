n = int(input())
lst = list(map(int,input().split()))

max_tmp = 0
ans = 0

for i in range(n):
    max_tmp = max(max_tmp, lst[i])
    ans = ans + (max_tmp - lst[i])

print(ans)