
def BubbleSort(A, N):
    cnt = 0 # swap???????????£????????°????¨???????????????°
    flag = 1 # flag = 1????????????????????????????????£??????????????¨?????????

    while flag:
        flag = 0

        for j in range(N - 1, 0, -1):
            if A[j] < A[j - 1]:
                A[j] , A[j - 1] = A[j - 1], A[j]
                cnt += 1
                flag = 1

    # swap???????????£????????°?????????
    return cnt


N = int(input())
A = [int(a) for a in input().split()]

cnt = BubbleSort(A, N)

print(*A)
print(cnt)