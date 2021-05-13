n = int(input())
A = list(map(int,input().split()))

S=[0]*n
for i in range(len(A)):
    S[A[i]-1] = i+1

for s in S:
    print(s,end=" ")