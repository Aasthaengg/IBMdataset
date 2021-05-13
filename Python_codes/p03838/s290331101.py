x, y = map(int, input().split())

cand = [(-x, y, 1), (x, y, 0), (-x, -y, 2), (x, -y, 1)] 

ans = 10e9
for a, b, c in cand:
    if a <= b:
        if ans > b - a + c:
            ans = b - a + c

print(ans)


