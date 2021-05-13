N = input()
A = map(int,raw_input().split())

x = 0

for i in range(N):
    minj = i
    y = 0
    for j in range(i,N):
        if A[j] < A[minj]:
            minj = j
            y = 1
            
    v = A[i]
    A[i] = A[minj]
    A[minj] = v
    x += y
    
for i in range(N-1):
    print A[i],
print A[-1]

print x