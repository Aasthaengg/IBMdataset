import sys
N=int(input())
T=[int(i) for i in input().split()]
A=[int(i) for i in input().split()]

if T[-1] != A[0]:
    print(0)
    sys.exit()

max_=T[-1]
MAX_T=[max_ for _ in range(N)]
MIN_T=[1 for _ in range(N)]
MAX_A=[max_ for _ in range(N)]
MIN_A=[1 for _ in range(N)]

MAX_T[0] = T[0]
MIN_T[0] = T[0]
for i in range(1,N):
    MAX_T[i] = T[i]
    if T[i] > T[i-1]:
        MIN_T[i] = T[i]
    else:
        MIN_T[i] = 1 

#print(MAX_T)
#print(MIN_T)   
        
MAX_A[-1] = A[-1]
MIN_A[-1] = A[-1]
for i in range(0,N-1)[::-1]:
    MAX_A[i] = min(MAX_A[i],A[i])
    if A[i] > A[i+1]:
        MIN_A[i] = min(MAX_A[i],A[i])
    else:
        MIN_A[i] = max(1,MIN_A[i])
        
#print(MAX_A)
#print(MIN_A)

sum_= 1
lim = 10**9 + 7
for i in range(N):
    if (MAX_T[i] < MIN_A[i]) or (MAX_A[i] < MIN_T[i]):
        print(0)
        sys.exit()
    else:
        sum_ = (sum_ * (min(MAX_T[i],MAX_A[i]) - max(MIN_T[i],MIN_A[i]) +1 )) % lim
print(sum_)