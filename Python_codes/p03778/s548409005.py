W, a, b = [int(x) for x in input().split()]

if abs(a - b) <= W:
    ans = 0
else:
    ans = min(abs(a + W - b), abs(a - b - W))

print (ans)