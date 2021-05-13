A = list(input())

if A[0] == A[1] == A[2] == 'R':
    print(3)
elif A[0] == A[1] == 'R' or A[1] == A[2] == 'R':
    print(2)
elif 'R' in A:
    print(1)
else:
    print(0)