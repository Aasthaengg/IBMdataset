n = input()
B = list(map(int,input().split()))
A = [B[0]]
for i,b in enumerate(B):
    A[i] = min(A[i],B[i])
    A.append(max(B[i],A[i]))

print(sum(A))
