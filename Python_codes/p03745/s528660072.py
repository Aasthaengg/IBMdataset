N=int(input())
A=list(map(int,input().split()))
flag=0
answer=1
if N==1:
    print(1)
else:
    if A[0] < A[1]:
        flag = 1
    elif A[0]>A[1]:
        flag = -1
    for n in range(N - 1):
        if flag == 1:
            if A[n] <= A[n + 1]:
                pass
            else:
                flag = 0
                answer += 1
        elif flag == -1:
            if A[n] >= A[n + 1]:
                pass
            else:
                flag = 0
                answer += 1
        else:
            if A[n] == A[n + 1]:
                pass
            elif A[n] < A[n + 1]:
                flag = 1
            else:
                flag = -1
    print(answer)
