# coidng : utf-8
n = int(input())
a = map(int, input().split())
max = -1000000
min = 1000000
sum = 0
for num in a:
    if max <= num:
        max = num
    if min >= num:
        min = num
    sum += num
print (min, max, sum)
