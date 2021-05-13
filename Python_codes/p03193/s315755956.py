N, H, W = map(int, input().split(' '))
lists = []
for i in range(N):
    lists.append(list(map(int, input().split(' '))))

count = 0

for list_ in lists:
    if H <= list_[0] and W <= list_[1]:
        count += 1

print(count)