from collections import deque
N = int(input())
A = list(map(int,input().split()))

B_even = deque([A[0]])
if N > 1:
    B_add = deque([A[1],A[0]])

for a_idx in range(2,len(A)):
    if a_idx % 2 == 0 :
        B_even.appendleft(A[a_idx])
        B_even.append(A[a_idx-1])
    else:
        B_add.appendleft(A[a_idx])
        B_add.append(A[a_idx-1])
        
if (N-1) % 2 ==0:
    B = B_even
else:
    B = B_add
    
print(' '.join(map(str,B)))