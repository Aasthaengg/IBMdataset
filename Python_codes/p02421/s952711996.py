#coding:utf-8
#1_9_C 2015.4.10
n = int(input())
taro = 0
hanako = 0

for i in range(n):
    cards = input().split()
    if cards[0] < cards[1]:
        hanako += 3
    elif cards[0] > cards[1]:
        taro += 3
    else:
        hanako += 1
        taro += 1
print(taro,hanako)