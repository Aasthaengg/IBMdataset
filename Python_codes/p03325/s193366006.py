n = int(input())
nums  = [int(i) for i in input().split()]

tmp = [i for i in nums if i % 2 == 0]
count = 0
for i in tmp:

    while i % 2 == 0:
        count += 1
        i //= 2

print(count)
