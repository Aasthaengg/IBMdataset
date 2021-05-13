n,q = map(int,input().split())
s = input()
LR = [0]*q
for i in range(q):
    
    LR[i] = list(map(int,input().split()))
A = [0]*n
for i in range(n-1):
    if s[i] == "A" and s[i+1] == "C":
        A[i+1] = 1
    A[i+1] += A[i]
for i in range(q):
    print(A[LR[i][1]-1]-A[LR[i][0]-1])