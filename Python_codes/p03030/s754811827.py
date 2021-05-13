N=int(input())
A = []
for i in range(N):
    s,p = input().split()
    p = int(p)
    A.append((s,p,i+1))
A = sorted(A,key=lambda x:x[1],reverse=True)
A = sorted(A,key=lambda x:x[0])
for i in range(N):
    s,p,k = A[i]
    print(k)