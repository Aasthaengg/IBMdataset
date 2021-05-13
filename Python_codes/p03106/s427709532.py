A, B, C = input().strip().split()
A, B, C = [int(A), int(B), int(C)]

L=[]
for i in range(min(A,B)):
    if A%(i+1) == 0 and B%(i+1) == 0:
        L.append(i+1)
print(L[len(L)-C])