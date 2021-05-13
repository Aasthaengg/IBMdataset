n = int(input())
a = list(map(int,input().split()))
a4 = []
a2 = []
odd = []
for i in range(n):
    if a[i] % 4 == 0:
        a4.append(a[i])
    elif a[i] % 2 == 0:
        a2.append(a[i])
    else:
        odd.append(a[i])
if len(a) > 3:
    if len(odd) <= len(a4):
        print('Yes')
    elif len(a2) == 0:
        if n %2 == 1 and len(odd) <= len(a4)+1:
            print('Yes')
        elif n%2 == 0 and len(odd) <= len(a4):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    if a4 or len(a2) == n:
        print('Yes')
    else:
        print('No')
    
