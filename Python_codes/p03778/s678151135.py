w, a, b = map(int, input().split())
aw = a + w
bw = b + w
print(b - aw if b > aw else (a - bw if a > bw else 0))