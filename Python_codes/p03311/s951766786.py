N = int(input())
A = list(map(int,input().split()))
B = [0]*N
for i in range(N):
    B[i] = A[i]-i-1
B.sort()
med = B[N//2]
loss = 0
for i in range(N):
    loss += abs(B[i]-med)
print(loss)
