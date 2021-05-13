n = int(input())
a = list(map(int,input().split()))

a = [x for x in a if x % 2 == 0]
a = [x for x in a if x % 3 != 0 and x % 5 != 0]

if len(a) == 0:
    print('APPROVED')
else:
    print('DENIED')

