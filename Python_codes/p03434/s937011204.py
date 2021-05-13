N=int(input())
A=[int(i) for i in input().split()]

Alice=0
Bob=0

for j in range(N):
    if j%2==0:
        Alice+=max(A)
        A.remove(max(A))
    
    else:
        Bob+=max(A)
        A.remove(max(A))
 
    
print(Alice-Bob)