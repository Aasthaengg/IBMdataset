n = int(input())
a = [int(_) for _ in input().split()]

a = [0] + a
ans = 0
for i in range(1, n+1):
    if a[a[i]] == i:
        ans += 1
print(ans//2)