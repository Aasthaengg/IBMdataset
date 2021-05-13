x = int(input())
cnt = 0
time = 0
for t in range(1, x + 1):
    cnt += t
    time += 1
    if cnt >= x:
        break
print(time)