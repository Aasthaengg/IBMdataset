N = int(input())
A = list(map(int, input().split()))
if(N == 1):
    print(1)
    exit(0)
cur = A[0]
# 昇順(1)か降順(0)かのフラグ
ans = 1
flag = -1
for i in range(1, N):
    if(cur == A[i]): continue
    if(flag == -1):
        if(A[i] > cur): flag = 1
        elif(A[i] < cur): flag = 0
        cur = A[i]
        continue
    if(flag == 1 and A[i] < cur):
        cur, flag = A[i], -1
        ans += 1
        continue
    if(flag == 1 and A[i] > cur):
        cur = A[i]
        continue
    if(flag == 0 and A[i] > cur):
        cur, flag = A[i], -1
        ans += 1
        continue
    if(flag == 0 and A[i] < cur):
        cur = A[i]
        continue
print(ans)
