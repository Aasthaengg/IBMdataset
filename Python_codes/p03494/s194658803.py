s = int(input())
s = input().rstrip().split(' ')

result = 0


def half(num):
    count = 0
    while ((num % 2) == 0) :
        num = num / 2
        count += 1
    return count


for num in s:
    num = int(num)
    count = half(num)
    if not result:
        result = count

    if count == 0:
        result = 0
        break

    if count < result:
        result = count

print(result)

