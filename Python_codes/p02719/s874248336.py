n,k = map(int,input().split())

S=[]
n1=n%k
S.append(n)
S.append(n1)
for i in range(10):
    n1=abs(n1-k)
    S.append(n1)
  
# print( n, n1, S )
print( min(S) )