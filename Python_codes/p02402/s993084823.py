n = int(input())
lis = list(map(int, input().split(" ")))
big_num = 1000000
max_num, min_num, sum = -1*big_num, big_num, 0
for i in lis:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
    sum += i
print("%d %d %d" % (min_num, max_num, sum))
