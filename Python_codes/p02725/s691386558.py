K,N=map(int,input().split())
A=list(map(int,input().split()))
lis=[]
for i in range(N-1):
    L=A[i+1]-A[i]
    lis.append(L)
lis.append(K-A[N-1]+A[0])
lis_sort=sorted(lis,reverse=True)
print(sum(lis_sort)-lis_sort[0])