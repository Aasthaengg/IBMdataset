from collections import deque
n = int(input())
A = deque(map(int, input().split()))
A.appendleft(0)
A.append(0)
ans = 0
for i in range(1, n+2):
    ans+=abs(A[i]-A[i-1])
for i in range(1, n+1):
    d = abs(A[i]-A[i-1])+abs(A[i+1]-A[i])
    print(ans-d+abs(A[i-1]-A[i+1]))
