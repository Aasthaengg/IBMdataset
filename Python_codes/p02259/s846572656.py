n = int(input())

list = [int(i) for i in input().split()]

def bubble(list):
    flag = 1
    count = 0
    while flag == 1:
        flag = 0
        for i in range(len(list)-1):
            if list[len(list)-1-i] < list[len(list)-1-i-1]:
                x = list[len(list)-i-1]
                list[len(list)-1-i] = list[len(list)-1-i-1]
                list[len(list)-1-i-1] = x
                flag = 1
                count += 1
    return [list,count]

answer = bubble(list)
for i in range(len(answer[0])):
    print(str(answer[0][i]) + ' ',end='') if i != len(answer[0])-1 else print(answer[0][i])
print(answer[1])