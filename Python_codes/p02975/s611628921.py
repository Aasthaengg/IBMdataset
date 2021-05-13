n = int(input())
a = list(map(int, input().split()))
A = sorted(set(a))
if len(A) == 1 and A[0] == 0:
    print('Yes')
else:
    if n % 3 == 0:
        if len(A) == 2 and A[0] == 0 and a.count(A[0]) * 2 == a.count(A[1]):
            print('Yes')
        elif len(A) == 3 and bin(A[0]^A[1]) == bin(A[2]) and a.count(A[0]) == a.count(A[1]) == a.count(A[2]):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
