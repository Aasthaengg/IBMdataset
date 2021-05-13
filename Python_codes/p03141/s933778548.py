N = int(input())
A = []
for i in range(N):
    a,b = map(int,input().split())
    A.append((a,b,a+b))
A = sorted(A,key=lambda x:x[2],reverse=True)
a = 0
for i in range(N):
    if i%2==0:
        a += A[i][0]
    else:
        a -= A[i][1]
print(a)