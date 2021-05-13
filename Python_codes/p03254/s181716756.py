n, x = map(int, input().split())
num_lists = list(map(int, input().split()))

num_lists.sort()
cnt = 0
sum = 0
for i in range(len(num_lists)):
    sum += num_lists[i]
    if sum <= x:
        cnt = i+1
    else:
        x = 0
        cnt = i
        break
x -= sum

if 0 < x:
    cnt -= 1

print(cnt)