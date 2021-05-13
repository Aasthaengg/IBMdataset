N = int(input())
A = []
if N%2==0:
    for i in range(1,N):
        for j in range(i+1,N+1):
            if j!=N+1-i:
                A.append((i,j))
else:
    for i in range(1,N):
        for j in range(i+1,N+1):
            if j!=N-i:
                A.append((i,j))
print(len(A))
for a in A:
    print(a[0],a[1])