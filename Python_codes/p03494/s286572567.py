n = int(input())
numbers = list(map(int, input().split()))

def div(x):#各要素を2で割って返す関数
    return x/2

count = 0
while 1:
    flag = 0
    for num in numbers:
        if num % 2:#2で割り切れない
            flag=1
            break
    if flag==1:
        break
    count += 1
    numbers = list(map(div,numbers))

print(count)
