n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    if a <= sum([int(i) for i in str(i)]) <= b:
        ans += i
else:
    print(ans)