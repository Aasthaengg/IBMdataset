#coding: UTF-8

shuffle = []
while True:
    str = input()
    if str == '-':
        break
    m = int(input())
    for num in range(m):
        h = int(input())
        str = str[h:] + str[:h]
    shuffle.append(str)

for i in range(len(shuffle)):
    print(shuffle[i])
