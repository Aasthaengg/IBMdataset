a,b,k = map(int,input().split())
n=max(a,b)
A=[]
for i in range(1,n+1):
    if  a%i==b%i==0:
         A.append(i)
A.sort(reverse = True)

print(A[k-1])
