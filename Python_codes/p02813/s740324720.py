import math
N = int(input())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]
S = [P, Q]
p = [0]*N
q = [0]*N

for i in range(N):
    for j in range(i):
        if P[i] > P[j]:
            p[i] += 1    
        if Q[i] > Q[j]:
            q[i] += 1

ans_p = 0
ans_q = 0

for i in range(N):
    ans_p += math.factorial(N-1-i) * (P[i]-1-p[i])
    ans_q += math.factorial(N-1-i) * (Q[i]-1-q[i])

print(abs(ans_p - ans_q))