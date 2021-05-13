#coding:utf-8
n = int(input())
numbers = list(map(int,input().split()))

print(*numbers)

for i in range(1,n):
    tmp = numbers[i]
    j = i - 1

    while j >= 0 and numbers[j] > tmp:
        numbers[j+1] = numbers[j]
        j -= 1
    numbers[j+1] = tmp

    print(*numbers)