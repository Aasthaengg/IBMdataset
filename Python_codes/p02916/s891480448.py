input()
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
pts = 0
prev = 0
for i in range(len(A)):
    try:
        pts += B[A[i] - 1]
    except:
        pass
    try:
        if prev+1 == A[i]:
            pts += C[A[i-1]-1]
    except:
        pass
    prev = A[i]
print(pts)