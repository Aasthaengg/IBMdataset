n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    if i%2 == 0 and a[i]%2 == 1: ans += 1
print(ans)