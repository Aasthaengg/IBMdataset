N = input()

a =  list(map(int,input().split()))
b = 0
c = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        b+=1
        if a[i] % 3 == 0 or a[i] % 5 == 0:
            c+=1
if b == c:
    print('APPROVED')
else:
    print('DENIED')