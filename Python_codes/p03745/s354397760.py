import sys
N = int(input())
A = [int(x) for x in input().split()]
if N == 1:
    print(1)
    sys.exit()
 
inc = 0  # 1: 単調非減少,　-1 : 単調非増加, 0: 未確定
ans = 1
for i in range(N - 1):
    if A[i] < A[i + 1]:
        if inc == -1:
            ans += 1
            inc = 0
        elif inc == 0:
            inc = 1
    elif A[i] > A[i + 1]:
        if inc == 1:
            ans += 1
            inc = 0
        elif inc == 0:
            inc = -1
 
print(ans)