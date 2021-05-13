n = list(input())
num = ['1', '9']
[print(num[num.index(i)-1], end='') for i in n]