n = int(input())
a = list(map(int, input().split()))

cnt = 1
first = True
increasing = True

for i in range(1, n):
    if (first):
        if (a[i] > a[i-1]):
            first = False
            increasing = True
        elif (a[i] < a[i-1]):
            first = False
            increasing = False
    else:
        if (a[i] > a[i-1]) and (increasing == False):
            cnt += 1
            first = True
        elif (a[i] < a[i-1]) and (increasing == True):
            cnt += 1
            first = True

print(cnt)