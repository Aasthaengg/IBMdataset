N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(A) > sum(B):
    print('No')
    exit()
else:
    cnt = sum(B)-sum(A)
a_tmp = 0
b_tmp = 0
for i in range(N):
    if A[i] == B[i]:
        continue
    if cnt == 0:
        print('No')
        exit()
    if A[i] > B[i]:
        b_tmp += A[i]-B[i]
    else:
        if (B[i]-A[i]) % 2 == 0:
            a_tmp += (B[i]-A[i]) // 2
        else:
            a_tmp += ((B[i]-A[i]) // 2)+1
            b_tmp += 1
if a_tmp > cnt or b_tmp > cnt:
    print('No')
    exit()
if (cnt-a_tmp)*2 == cnt-b_tmp:
    print('Yes')
else:
    print('No')