x, y = map(int, input().split())
cnt = 0
ai = x
for i in range(2**60):
    if ai <= y:
        cnt += 1
        ai *= 2
    else:
        break
print(cnt)