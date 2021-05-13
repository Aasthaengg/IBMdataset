n = int(input())
A = list(map(int, input().split()))

max_a = max(A)
min_a = min(A)

max_a_ind = A.index(max_a)
min_a_ind = A.index(min_a)

if min_a >= 0:
    check = 'sei'
elif max_a > 0 and min_a < 0:
    check = 'seifu'
else:
    check = 'fu'

if check == 'sei':
    print(n-1)
    for i in range(n-1):
        print(str(i+1) + ' ' + str(i+2))
elif check == 'fu':
    print(n-1)
    for i in range(n-2, -1, -1):
        print(str(i+2) + ' ' + str(i+1))
else:
    if abs(max_a) >= abs(min_a):
        print(n+n-1)
        for i in range(n):
            print(str(max_a_ind+1) + ' ' + str(i+1))
        for i in range(n-1):
            print(str(i+1) + ' ' + str(i+2))
    else:
        print(n+n-1)
        for i in range(n):
            print(str(min_a_ind+1) + ' ' + str(i+1))
        for i in range(n-2, -1, -1):
            print(str(i+2) + ' ' + str(i+1))