n = int(input())
ans = float('inf')
for a in range(1, n):
    b = list(str(n - a))
    a = list(str(a))
    ans = min(ans, sum(list(map(int, a)) + list(map(int, b))))
print(ans)