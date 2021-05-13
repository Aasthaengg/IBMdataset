n = int(input())
a = [int(input()) for _ in range(n)]

a.sort()
count = 0
temp = a[0]
tempcount = 1
for i in range(1,n):
    if a[i]==temp:
        tempcount += 1
    else:
        if not tempcount%2 == 0:
            count += 1
        tempcount = 1
    temp = a[i]
    #print(i,tempcount)
if tempcount%2 == 1:
    count += 1
print(count)