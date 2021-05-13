n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

flag = True
for i in range(n - 1):
    if a[i + 1] - a[i] >= 2:
        flag = False
if a[0] != 0:
    flag = False

count = 0
if flag == True:
    for i in range(n - 1):
        if a[i] != 0:
            count = count + 1
        if a[i] >= a[i + 1]:
            count = count + max(0, a[i + 1] - 1)
   
if flag == False:
    print(-1)
elif a[n - 1] != 0:
    print(count + 1)
else:
    print(count)