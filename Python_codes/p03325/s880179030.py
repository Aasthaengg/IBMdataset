input()
cnt = 0
for i in map(int, input().split()):
    while i % 2 == 0:
        i //= 2
        cnt += 1
print(cnt)