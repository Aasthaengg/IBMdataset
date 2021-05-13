A = map(int, input().split())

A_sum = sum(A)

if A_sum >= 22:
    print('bust')
else:
    print('win')