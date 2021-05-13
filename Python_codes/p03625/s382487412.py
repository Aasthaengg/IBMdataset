N = int(input())
A = list(map(int,input().split()))
A = sorted(A, reverse = True)
t = 0
y = 0
cnt = 0
for i in range(len(A)-1):
    if A[i] == A[i+1]:
        t = A[i]
        break
    cnt += 1
for j in range(len(A)-1):
    if A[j] == A[j+1] and j >= cnt+2:
        y = A[j]
        break
print(t*y)
