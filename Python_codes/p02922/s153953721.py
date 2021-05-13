A, B = [int(x) for x in input().split(" ")]

count = 0
nums = 1
while nums < B:
    nums += A - 1
    count += 1

print(count)
