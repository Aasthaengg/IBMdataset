N = int(input())
a = [int(input()) for _ in range(N)]

log = []
button = 1
count = 0
while button != 2:
    button = a[button-1]
    count += 1
    log.append(button)
    if count == N+1:
        count = -1
        break
print(count)