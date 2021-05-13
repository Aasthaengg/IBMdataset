
N = int(input())

A = list(map(int,input().split()))

#%%

A.sort()

keyz = 0
for a in A:
    if a<0:
        keyz += 1

if keyz==0:
    keyz = 1
elif keyz == N:
    keyz = N-1


M = 0
M += -sum(A[:keyz])
M += sum(A[keyz:])
print(M)

# A[0:keyz]までを負とする
    

# A[keyz:]は反転させる必要あり

if keyz == N-1:
    cur = A[-1]
    for i in range(N-1):
        print(cur,A[i])
        cur -= A[i]
    
else:            
    cur = A[0]
    for i in range(keyz,N-1):
        print(cur,A[i])
        cur = cur - A[i]
    print(A[N-1],cur)
    cur = A[N-1] - cur
    for i in range(1,keyz):
        print(cur,A[i])
        cur -= A[i]
        
        



