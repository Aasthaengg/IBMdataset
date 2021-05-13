N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cn = 0

for i in range(N):
    
    if B[i] <= A[i]:
        
        cn = cn + B[i]
    elif B[i] > A[i] and B[i] < (A[i]+A[i+1]) :
        cn = cn + B[i]
        A[i+1] = A[i+1] - (B[i] - A[i])
    elif B[i] >= A[i] + A[i+1]:
        cn = cn + A[i] + A[i+1]
        A[i] = 0
        A[i+1] = 0
        
      
print(cn)