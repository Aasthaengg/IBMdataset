N = int(input())
bricks = list(map(int, input().split()))

pos_num = 1
count = 0
for num in bricks:
    if num == pos_num:
        pos_num += 1
    else:
        count += 1

if count == N:
    print(-1)
else:
    print(count)