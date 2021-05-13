N = int(input())
P = list(map(int, input().split()))
min_n = N + 1
ans = 0
for pi in P:
    if pi <= min_n:
        ans += 1
        min_n = pi
print(ans)
