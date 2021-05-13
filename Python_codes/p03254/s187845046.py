N, x = map(int, input().split())
a = sorted(map(int, input().split()))
cnt = 0
for i in a:
    if x < i:
        break
    cnt += 1
    x -= i
else:
    if x > 0:
        cnt -= 1
print(cnt)