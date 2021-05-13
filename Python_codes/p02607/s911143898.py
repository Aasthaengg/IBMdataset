n = int(input())
a = [int(x) for x in input().split()]

ans = 0
for i in range(n):
    if i % 2 == 0:
        if a[i] % 2 == 1:
            ans += 1

print(ans)