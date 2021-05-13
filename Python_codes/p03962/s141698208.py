A = list(map(int, input().split()))
if A.count(A[0]) == 3:
    print("1")
elif A.count(A[0]) == 2:
    print("2")
elif A.count(A[0]) == 1:
    if A.count(A[1]) == 1:
        print("3")
    else:
        print("2")
