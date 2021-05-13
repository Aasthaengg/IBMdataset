a, b, c = map(int, input().split())
can = a + b + 1
doku = 0
if can >= c:
    doku = c
else:
    doku = can
ans = b + doku
print(ans)
