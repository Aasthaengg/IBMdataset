go = 1
while go == 1:
    a = str(input())
    alist = list(a)
    if a == "0":
        go = 0
        exit
    sum = 0
    for i in alist:
        i = int(i)
        sum += i
    if go == 1:
        print(sum)
