N = int(input())
A = list(map(int, input().split()))

A = sorted(A)

set_A = set(A)
if len(set_A) == 1:
    print(len(A))
    exit()
    
tmp_slime = A[0]
tmp_flag = True
for i in range(1, len(A)):
    if tmp_slime*2 >= A[i]:
        tmp_slime += A[i]
    else:
        tmp_flag = False
        break
if tmp_flag:
    print(len(A))
    exit()

low = 0
high = len(A)-1
mid = (low + high) // 2
while True:
    tmp = mid
    slime = sum(A[0:mid+1])
    flag = True
    for i in range(mid+1, len(A)):
        if slime*2 >= A[i]:
            slime += A[i]
        else:
            flag = False
            break
    if flag:
        high = mid
        mid = (low + high) // 2
    else:
        low = mid
        mid = (low + high) // 2
    if mid == tmp:
        break
    
print(len(A) - len(A[0:mid+1]))
