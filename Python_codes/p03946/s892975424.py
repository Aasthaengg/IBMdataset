N,T = map(int,input().split())
A = list(map(int,input().split()))
C = {}
amin = A[0]
for i in range(1,N):
    a = A[i]
    if a>amin:
        b = a-amin
        if b not in C:
            C[b] = []
        C[b].append(i)
    elif a==amin:
        continue
    else:
        amin = a
C = sorted(list(C.items()),key=lambda x:x[0],reverse=True)
print(len(C[0][1]))