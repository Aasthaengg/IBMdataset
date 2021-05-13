N,*A = map(int, open(0).read().split())
ans = 1
if N <= 2:
    print(1)
else:
    if A[1] > A[0]:
        dif = 1
    elif A[1] < A[0]:
        dif = -1
    else:
        dif = 0
    for i in range(2,N):
        if A[i] > A[i-1]:
            if dif == -1:
                ans += 1
                dif = 0
            elif dif == 0:
                dif = 1
        elif A[i] < A[i-1]:
            if dif == 1:
                ans += 1
                dif = 0
            elif dif == 0:
                dif = -1
    print(ans)