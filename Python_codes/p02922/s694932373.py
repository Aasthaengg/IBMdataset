a, b = list(map(int, input().split()))
c = 1
cnt = 0
while(True):
    if c >= b:
        break
    c += a - 1
    cnt += 1

print(cnt)
