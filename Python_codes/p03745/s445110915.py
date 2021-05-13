import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))


ans = 1
state = -1
for i in range(1, N):
    if state == -1:
        if A[i] < A[i-1]:
            state = 0
        elif A[i] > A[i-1]:
            state = 1
    elif (state == 0 and A[i] > A[i-1]) or (state == 1 and A[i] < A[i-1]):
        ans += 1
        state = -1
 
print(ans)