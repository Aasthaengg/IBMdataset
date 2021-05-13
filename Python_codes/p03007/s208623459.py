N = int(input())
A = list(map(int, input().split()))

A = sorted(A)

count_m = 0
count_z = 0
count_p = 0
sum_abs = 0

for i in range(N):
    if A[i] < 0:
        count_m += 1
        sum_abs -= A[i]
    elif A[i] == 0:
        count_z += 1
    else:
        count_p += 1
        sum_abs += A[i]

if count_m + count_z == 0:
    print(sum_abs-2*min(A))
    tmp = A[0]
    for i in range(N-2):
        print(tmp, A[i+1])
        tmp -= A[i+1]
    print(A[-1], tmp)

elif count_p + count_z == 0:
    print(sum_abs+2*max(A))
    tmp = A[-1]
    for i in range(N-1):
        print(tmp, A[i])
        tmp -= A[i]

elif count_p + count_m == 0:
    print(0)
    for i in range(N-1):
        print(0, 0)

else:
    print(sum_abs)
    cmz = count_m + count_z
    tmp = A[-1]
    for i in range(cmz - 1):
        print(tmp, A[i])
        tmp -= A[i]
    tmp_2 = A[cmz-1]
    if count_p != 0:
        for i in range(count_p-1):
            print(tmp_2, A[i+cmz])
            tmp_2 -= A[i+cmz]
        print(tmp, tmp_2)