import itertools

N = int(input())
A = list(map(int,input().split()))
A.sort()
B = list(itertools.accumulate(A))
jdg = 0

for i in range(1,N):
    if A[i] > B[i-1]*2:
        #print(A[i],B[i-1])
        jdg = i
print(N-jdg)