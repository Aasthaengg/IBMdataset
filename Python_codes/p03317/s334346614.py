n, k  = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

count = 0

while n > 0:
    if n > k:
        n -= k-1
    else:
        n -= k
    count += 1

print(count)


