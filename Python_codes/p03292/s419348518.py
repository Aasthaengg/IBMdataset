A = list(map(int, input().split())) 
A.sort()
mini = A[0]
maxi = A[len(A)-1]
print(maxi-mini)