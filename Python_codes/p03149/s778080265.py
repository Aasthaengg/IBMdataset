n = list(map(int, input().split()))

if sorted(n) == sorted([1, 9, 7, 4]):
    ans = "YES"
else:
    ans = "NO"

print(ans)
