n = int(input())
a = list(map(int, input().split()))
num = 0
count = 1
mode = 0
while num < n - 1:
    if a[num] == a[num + 1]:
        num += 1
    elif a[num] > a[num + 1]:
        num += 1
        if mode == -1:
            pass
        elif mode == 0:
            mode = -1
        else:
            count += 1
            mode = 0
    else:
        num += 1
        if mode == 1:
            pass
        elif mode == 0:
            mode = 1
        else:
            count += 1
            mode = 0
print(count)