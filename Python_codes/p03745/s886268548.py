N  = int(input())
A = list(map(int, input().split()))
status = 0 # 0 = defalt, 1 = up, 2 = down
cnt = 1
for i in range(1,N):
    if A[i-1] < A[i]: #up petern
        if status == 0 or status == 1:
            status = 1
        else:
            status = 0
            cnt += 1
    elif A[i-1] > A[i]:
        if status == 0 or status == 2:
            status = 2
        else:
            status = 0
            cnt += 1
    else:
        continue
print(cnt)