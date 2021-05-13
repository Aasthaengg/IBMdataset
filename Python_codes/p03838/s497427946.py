x, y = map(int, input().split())
cnt = 0
diff = abs(x) - abs(y)
if diff == 0:
    if x * y < 0:
        cnt += 1
elif diff > 0:
    cnt += diff
    if x > 0:
        cnt += 1
    if y > 0:
        cnt += 1
else:
    cnt += -diff
    if x < 0:
        cnt += 1
    if y < 0:
        cnt += 1
print(cnt)
