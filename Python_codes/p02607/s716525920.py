n = int(input())

cnt = 0
for a in input().split(' ')[::2]:
    if int(a) % 2 == 1:
        cnt += 1

print(cnt)