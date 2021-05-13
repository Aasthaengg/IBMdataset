n = int(input())
flag = 0
while n>0:
    if n % 4 == 0:
        flag = 1
        break
    n -= 7
    if n == 0:
        flag=1
        break
print('Yes' if flag == 1 else 'No')
