N = int(input())
A = list(map(int, input().split()))

lst = []
for i in A:
    if i % 2 == 0:
        lst.append(i)
lst2 = []
if lst:
    for j in lst:
        if j % 3 == 0 or j % 5 == 0:
            lst2.append(j)
    if lst == lst2:
        print('APPROVED')
    else:
        print('DENIED')
else:
    print('APPROVED')