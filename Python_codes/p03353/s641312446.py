S = input()
K = int(input())

A = []
for i in range(len(S)):  
    for j in range(1,i + 6):
        if S[i:j] != "":
            A.append(S[i:j])

A = sorted(set(A))
        
print(A[K-1])