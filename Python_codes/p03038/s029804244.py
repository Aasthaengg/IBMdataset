from collections import deque

N,M = list(map(int,input().split()))
A = list(map(int,input().split()))

BC_dict={}
for m in range(M):
    b,c = list(map(int,input().split()))
    if c in BC_dict.keys():
        BC_dict[c]+=b  
    else:    
        BC_dict[c]=b  
    
C = list(BC_dict.keys())

A.sort()
C.sort(reverse=True)

C=deque(C)

check = C.popleft()

for a_idx,a in enumerate(A):
    if a >= check:
        break
    
    A[a_idx] = check
    BC_dict[check] -= 1
    
    if BC_dict[check] == 0:
        if len(C) == 0:
            break
        else:
            check = C.popleft()
        
print(sum(A))