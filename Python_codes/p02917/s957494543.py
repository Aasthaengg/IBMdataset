n = int(input())
lb = [int(w) for w in input().split()]

ans = 0

if n - 1 == 1:
    ans = lb[0]*2
else:
    ans += lb[0]
    for i in range(n - 2):
        ans += min(lb[i:i + 2])
    ans += lb[n - 2]

print(ans)
