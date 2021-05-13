n, a, b = map(int, input().split())
c = abs(a-b)
if c % 2 == 0:
    ans = "Alice"
else:
    ans = "Borys"
print(ans)