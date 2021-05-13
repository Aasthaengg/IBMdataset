n = int(input())
a = list(map(int,input().split()))

count = 1
flag = 0

for i in range(len(a)-1):
    if flag == 1:
        if a[i] > a[i+1]:
            flag = 0
            count += 1
    elif flag == -1:
        if a[i] < a[i+1]:
            flag = 0
            count += 1
    else:
        if i == len(a)-1:
            count+1
        elif a[i] < a[i+1]:
            flag = 1
        elif a[i] > a[i+1]:
            flag = -1

print(count)