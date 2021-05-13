n = int(raw_input())
a = map(int, raw_input().split())

flag = 1
count = 0
while flag:
    flag = 0
    for j in range(n-1, 0, -1):
        if a[j] < a[j-1]:
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp
            count += 1
            flag = 1
            #print a

for i in range(n):
    if i == n -1:
        print a[i]
    else:
        print a[i],

print count