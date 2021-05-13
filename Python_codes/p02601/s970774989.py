red, green, blue = map(int, input().split())
k = int(input())

cnt = 0
while red >= green:
    green *= 2
    cnt += 1
while green >= blue:
    blue *= 2
    cnt += 1

if cnt <= k:
    print('Yes')
else:
    print('No')