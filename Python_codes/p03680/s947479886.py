N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
history = set()
now = 0
cnt = 0
while(True):
    if now in history:
        cnt = -1
        break
    else:
        cnt += 1
        history.add(now)
        now = a[now]-1
        if now == 1:
            break
print(cnt)