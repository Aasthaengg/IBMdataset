n = int(input())

numbers = list(map(int, input().split(" ")))

cnt = 0

flag = 1

si = 0

while flag:
    flag = 0
    for j in range(n - 1, si, -1):
        if numbers[j] < numbers[j - 1]:
            tmp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = tmp
            cnt += 1
            flag = 1

numbers = map(str, numbers)
print(" ".join(numbers))

print(cnt)