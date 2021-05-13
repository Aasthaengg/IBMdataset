n = int(input())
a = list(map(int,input().split()))
a.sort()
a.reverse()
count = 1
x = 0
y = 0
for i in range(1,n):
    if a[i] == a[i-1]:
        count+=1
    else:
        count = 1
    if count == 2 and x == 0:
        x = a[i]
        count = 0       
    elif count == 2 and y == 0:
        y = a[i]
print(x*y)