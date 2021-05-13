n, m = map(int, input().split())
ba = []
for i in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    ba.append((b,a))
ba.sort()
count = 0
prev_b = -1
for b, a in ba:
    if a < prev_b:
        continue
    prev_b = b
    count += 1
print(count)
