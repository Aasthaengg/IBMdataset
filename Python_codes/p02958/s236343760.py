N = int(input())
P = list(map(int,input().split()))
R = sorted(P)
import copy
answer = 'NO'
for i in range(0,N-1):
    for j in range(i+1,N):
        Q = copy.deepcopy(P)
        A = Q[i]
        B = Q[j]
        Q[i] = B
        Q[j] = A
        if Q == R:
            answer = 'YES'
            break
if P == R:
    answer = 'YES'
print(answer) 