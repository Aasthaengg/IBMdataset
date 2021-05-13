p = 10**9+7
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*(pow(x,(m-1)//2)**2)%p)%p
L = list(map(int,list(input().strip())))
N = len(L)
A = []
for i in range(N):
    if L[i]==1:
        A.append(i)
cnt = 0
for i in range(len(A)):
    j = A[i]
    k = i
    n = N-1-j
    cnt = (cnt+pow(2,k)*pow(3,n))%p
cnt = (cnt+pow(2,len(A)))%p
print(cnt)