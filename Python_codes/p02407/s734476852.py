# cording utf-8

num = int(input())
list = input().rstrip().split(" ")

num = num - 1
result = str(list[num])

for i in range(num):
    result = result + " " + str(list[num-1-i])

print(result)