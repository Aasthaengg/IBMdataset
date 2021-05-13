S = input().split()
A = int(S[0])
B = int(S[1])
K = int(S[2])
#print(A, B, K)

for k in range(K):
    if k % 2 == 0: #taka 
        if A % 2 == 1:
            A -= 1
        B_plus = A//2
        A -= B_plus
        B += B_plus
        #print(A, B)
    else:        
        if B % 2 == 1:
            B -= 1
        A_plus = B//2
        B -= A_plus
        A += A_plus
        #print(A, B)
        
print(A,B)
