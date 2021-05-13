import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(1,N):
    if A[i] - A[i-1] != 0:
        B.append(A[i] - A[i-1])
cnt = 0
for i in range(1,len(B)):
    if i >1:
        if B[i-1]*B[i-2] < 0 :
            continue
    if B[i]*B[i-1]<0:
        cnt += 1
        B[i]=0
        
print(cnt+1)