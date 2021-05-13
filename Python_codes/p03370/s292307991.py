n, x = map(int, input().split())

lis = []
for i in range(n):
    lis.append(int(input()))

lis = sorted(lis)
cnt = 0

for i in range(n):
    if x < lis[i]:
        print(cnt)
        exit()
    x = x - lis[i]
    cnt += 1

m = min(lis)

while x >= m:
    x -= m
    cnt += 1

print(cnt)