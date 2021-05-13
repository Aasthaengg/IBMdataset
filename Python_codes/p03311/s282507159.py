N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(N):
    A[i] -= i+1
A.sort()
#for i in range(N):
#    B.append(A[i]-i-1)
#B.sort()
med = N // 2
grief = 0
for i in range(N):
    grief += abs(A[i]-A[med])
#for i in range(N):
#    grief += abs(B[i]-B[med])
print(str(grief))