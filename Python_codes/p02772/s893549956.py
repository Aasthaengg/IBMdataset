N = int(input())
A = list(map(int, input().split()))

for i in A:
    if i % 2 == 0 and i % 3 != 0 and i % 5 != 0:
        result = 'No'
        break
    else:
        result = 'Yes'

if result == 'No':
    print('DENIED')
else:
    print('APPROVED')