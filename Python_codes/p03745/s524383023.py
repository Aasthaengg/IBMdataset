N = int(input())
A = list(map(int,input().split()))
bol = 0
cnt = 1
for i in range(N-1):
    if bol == 0:
        if A[i] > A[i+1]:
            bol = -1
        elif A[i] < A[i+1]:
            bol = 1
    elif bol == 1:
        if A[i] > A[i+1]:
            cnt += 1
            bol = 0
    else:
        if A[i] < A[i+1]:
            cnt += 1
            bol = 0
print(cnt)