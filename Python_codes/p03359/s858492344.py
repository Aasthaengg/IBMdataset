a, b = map(int, input().split())
cnt = 0
if a <= b:
    cnt += a
else:
    cnt += a-1
print(cnt)
