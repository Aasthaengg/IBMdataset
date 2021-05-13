n, x = map(int, input().split())
l = list(map(int, input().split()))
sum = 0
cnt = 1

for e in l:
    sum += e
    if sum > x:
        break
    cnt += 1

print(cnt)