a, b, c = map(int, input().split())
eo = (a + b + c) % 2
lv = max(a, b, c) * 3
tgt = (lv if lv % 2 == eo else lv + 3)
print((tgt - (a + b + c)) // 2)