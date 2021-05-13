n = int(input())
a = [int(i) for i in input().split()]
con =0
ex = -1
for i in range(n):
    if a[i] % 4 == 0:
        con +=1
    elif a[i] % 2 == 0:
        ex +=1
    
if ex == -1:
    ex = 0
if (n-ex)//2 <= con:
    print('Yes')
else:
    print('No')