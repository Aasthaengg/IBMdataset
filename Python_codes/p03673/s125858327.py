from collections import deque
n = int(input())
A = deque(map(int, input().split()))
b = deque([])

if n%2==0:
    for i in range(n):
        if i%2 ==0:
            b.append(A[i])
        else:
            b.appendleft(A[i])
else:
    for i in range(n):
        if i%2 ==0:
            b.appendleft(A[i])
        else:
            b.append(A[i])            
print(*b)