N,K = map(int,input().split())

T = []

for i in range(N):
    t = int(input())
    T.append(t)

T.sort()

A = float("infinity") 
for i in range(N-K+1):
    a = T[i+K-1] - T[i]
    A = min(A,a)

print(A)