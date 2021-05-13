n = int(input())
a = [int(s) for s in input().split()]

ans = 0
for i in range(n):
    if a[a[i]-1] == i + 1:
        ans += 1
print(ans // 2)
