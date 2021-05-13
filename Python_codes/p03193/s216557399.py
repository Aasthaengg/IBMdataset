n, h ,w = list(map(int, input().split()))
li = [list(map(int, input().split())) for i in range(n)]

count = 0
for i in range(n):
    if li[i][0] >= h and li[i][1] >= w:
        count += 1

print(count)