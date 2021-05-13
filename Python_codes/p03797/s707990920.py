s, c = map(int, input().split())

cnt = 0
if s <= c // 2: 
    cnt += s
    c -= 2 * s
    s = 0
else:
    cnt += c // 2
    s -= c // 2
    c = 0

cnt += c // 4

print(cnt)