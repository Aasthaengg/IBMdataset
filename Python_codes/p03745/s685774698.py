N = int(input())
A = list(map(int,input().split()))
count = 1
increase = False
decrease = False
for i in range(1,N):
    if A[i-1] == A[i]:
        continue
    elif increase and A[i-1] < A[i]:
        continue
    elif decrease and A[i-1] > A[i]:
        continue
    elif not increase and not decrease and A[i-1] < A[i]:
        increase = True
    elif not increase and not decrease and A[i-1] > A[i]:
        decrease = True
    else:
        count += 1
        increase = False
        decrease = False
print(count)