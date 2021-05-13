n = int(input())
a_list = list(map(int, input().split()))

status = True
execute = 0
while status:
    for i in range(n):
        if a_list[i] % 2 == 1:
            status = False
            break
        else:
            a_list[i] = a_list[i] / 2
    if status:
        execute += 1
print(execute)
