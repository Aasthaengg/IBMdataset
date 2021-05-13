n, a, b = map(int, input().split())
ans = 0
for i in range(1, n+1):
    s = str(i)
    sums = 0
    for x in s:
        sums += int(x)
    if a <= sums and sums <= b:
        ans += i
print(ans)